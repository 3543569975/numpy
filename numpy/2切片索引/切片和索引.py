import numpy as np

#创建ndarray对象
ar_np = np.arange(10)
#从索引2开始到索引7停止，间隔为2
s = slice(2,7,2)
print('np.arange:  {}'.format(ar_np))
print('切片和索引:  {}'.format(ar_np[s]))

#正常索引切片

#整数数组的索引
np_ar = np.array([[1,2],[3,4],[5,6]])
print('初始数组：  {}'.format(np_ar))
#获取坐标轴为（0，0），（1，1），（2，0）的元素
point_ar = np_ar[[0,1,2],[0,1,0]]
print('获取的元素：  {}'.format(point_ar))

np_ar = np.array([[1,2,3],[4,5,6],[7,8,9]])
s1_ar = np_ar[1:3,1:3]
print('s1_ar获取的元素：\n  {}'.format(s1_ar))

s2_ar = np_ar[1:3,[1,2]]
print('s2_ar获取的元素：\n  {}'.format(s2_ar))

s3_ar = np_ar[...,1:]
print('s3_ar获取的元素：\n  {}'.format(s3_ar))