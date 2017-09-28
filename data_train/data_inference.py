#coding=utf-8
#test
import tensorflow as tf 
import numpy as np

b_cell=[0.1,-0.1]

bias1=0.0
bias2=0.0

def inference(input_tensor,train,regularizer):
	with tf.variable_scope('layer'):
		state=tf.get_variable('state',[1,2],initializer=tf.constant_initializer(0.0))
		w_cell_state=tf.get_variable('weight1',[2,2],initializer=tf.truncated_normal_initializer(stddev=0.1))
		w_cell_input=tf.get_variable('weight2',[1,2],initializer=tf.truncated_normal_initializer(stddev=0.1))
		w_output=tf.get_variable('weight3',[2,1],initializer=tf.truncated_normal_initializer(stddev=0.1))
		b_output=tf.get_variable('weight4',[1],initializer=tf.constant_initializer(0.1))

		weight1=tf.get_variable('weight5',[1,3],initializer=tf.truncated_normal_initializer(stddev=0.1))
		weight2=tf.get_variable('weight6',[1,12],initializer=tf.truncated_normal_initializer(stddev=0.1))

		final_logit=[]
		for h in range(100):
			data=input_tensor[h]
			fc2=[]
			for i in range(12):
				row=data[i]
				fc1=[]
				for j in range(3):
					x=row[j]
					before_activation=tf.matmul(state,w_cell_state)+x*w_cell_input+b_cell
					state=tf.tanh(before_activation)
					output=tf.matmul(state,w_output)+b_output
					fc1.append(output)
				final_output=tf.tanh(tf.matmul(weight1,fc1)+bias1)
				fc2.append(final_output)
			logit=tf.matmul(weight2,fc2)+bias2
			final_output.append(logit)
		if regularizer != None:
			tf.add_to_collection('losses',regularizer(weight1)+regularizer(weight2))
		return fianl_logit