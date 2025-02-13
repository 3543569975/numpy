import numpy.matlib
import numpy as np


#empty(shape,dtype,order):shape（定义矩阵形状的整数或整数元组）dtype（数据类型）order（c行序优先，f列）
#填充为随机数据
print(np.matlib.empty((2,2)))

#zeros:创建一个以0为填充的矩阵
print(np.matlib.zeros((2,2)))

#ones:创建一个以0填充的矩阵
print(np.matlib.ones((2,2)))

#eye(n,m,k,dtype):n(返回矩阵的行数)m(返回矩阵的列数)k(对角线的索引)dtype(数据类型)
print(np.matlib.eye(3,4,0,float))

#identity:返回给定大小的单位矩阵
#大小为2，类型整型
print('整型单位矩阵：\n{}'.format(np.matlib.identity(2,float)))

#rand:创建一个给定大小的矩阵，数据随机填充
print('rand(随机数矩阵：\n{}'.format(np.matlib.rand(3,3)))