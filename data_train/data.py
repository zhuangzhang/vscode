#coding=utf-8
#导入表
import xlrd

X=[]
Y=[]

DATA_NAME='1.xls'

fname=DATA_NAME
bk=xlrd.open_workbook(fname)
shxrang=range(bk.nsheets)
sh=bk.sheet_by_name('sheet1')
#获取行数
nrows=sh.nrows

#获取各行数据
row_list=[]
for i in range(0,nrows):
	row_data=sh.row_values(i)
	row_list.append(row_data)
dataset=row_list

Y=[]
X=[]
for i in range(nrows-1):
	X.append(dataset[i][0:36])
	Y.append(dataset[i][37])