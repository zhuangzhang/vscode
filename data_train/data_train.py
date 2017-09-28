#coding=utf-8
import os
import tensorflow as tf 
import numpy as np
#导入表库
import xlrd

import data_inference
import data

NUM_DATA=5000

#配置神经网络参数
BATCH_SIZE=100
LEARNING_RATE_BASE=0.1
LEARNING_RATE_DECAY=0.05
REGULARITION_RATE=0.0001
TRAINING_STEPS=30000
MOVING_AVERAGE_DECAY=0.99

#数据文件名
DATA_NAME='1.xls'
MODEL_SAVE_PATH='data/'
MODEL_NAME='model.ckpt'

def train(data):
	#定义输入输出
	x=tf.placeholder(tf.float32,[BATCH_SIZE,12,3],name='x-input')
	y_=tf.placeholder(tf.float32,[BATCH_SIZE,1],name='y-input')

	regularizer=tf.contrib.layers.l2_regularizer(REGULARITION_RATE)

	#直接使用data_inference.py中定义的传播过程
	y=data_inference.inference(x,train,regularizer)

	global_step=tf.Variable(0,trainable=False)

	#损失函数、学习率、滑动平均操作以及训练过程
	variable_averages=tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,global_step)
	variable_averages_op=variable_averages.apply(tf.trainable_variables())
	mes=tf.reduce_mean(tf.square(y_-y))
	loss=mes+tf.add_n(tf.get_collection('losses'))
	learning_rate=tf.train.exponential_decay(LEARNING_RATE_BASE,global_step,50,LEARNING_RATE_DECAY,staircase=True)
	train_step=tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,global_step=global_step)
	with tf.control_dependencies([train_step,variable_averages_op]):
		train_op=tf.no_op(name='train')

	#初始化TensorFlow持久化类
	saver=tf.train.Saver()
	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())

		for i in range(TRAINING_STEPS):
			start=(i*BATCH_SIZE) % NUM_DATA
			end=min(start+BATCH_SIZE,NUM_DATA)
			xs=data.X[start:end]
			ys=data.Y[start:end]
			reshaped_xs=np.reshape(xs,(BATCH_SIZE,12,3))
			reshaped_ys=np.reshape(ys,(BATCH_SIZE,1))
			_,loss_value,step=sess.run([train_op,loss,global_step],feed_dict={x:reshaped_xs,y_:reshaped_ys})

			#每1000轮保存一次模型
			if i % 1000 == 0:
				print('After %d training step(s),loss on training batch is %g' % (step,loss_value))

def main(argv=None):
	train(data)
if __name__ == '__main__':
	tf.app.run()