import numpy as np


#1为行，0为列
#amin:计算数组中元素沿指定轴的最小值
#amax:计算数组中元素沿指定轴的最大值
num_np= np.array([[3,7,5],[8,4,3],[2,4,9]])
print('初始数组：\n{}'.format(num_np))
print('amin:\n{}'.format(np.amin(num_np,1)))
print('amin:\n{}'.format(np.amin(num_np,0)))
print('amax:\n{}'.format(np.amax(num_np)))
print('amax:\n{}'.format(np.amax(num_np,axis=0)))

#ptp:计算数组中元素最大值与最小值的差
print('ptp:\n{}'.format(np.ptp(num_np)))
print('ptp1行:\n{}'.format(np.ptp(num_np,1)))
print('ptp0列:\n{}'.format(np.ptp(num_np,0)))

#percentile：百分位函数
num_np = np.array([[10,7,4],[3,2,1]])
print('初始数组：\n{}'.format(num_np))
#50%的分位数
print('50%:\n{}'.format(np.percentile(num_np,50)))
print('50%0列：\n{}'.format(np.percentile(num_np,50,0)))
print('50%1行：\n{}'.format(np.percentile(num_np,50,1)))
print('50%1行维度保持不变：\n{}'.format(np.percentile(num_np,50,1,keepdims=True)))

#median:计算数组中元素的中位数
num_np = np.array([[30,65,70],[80,95,10],[50,90,60]])
print('初始数组:\n{}'.format(num_np))
print('median:\n{}'.format(np.median(num_np)))
print('median0列：\n{}'.format(np.median(num_np,axis=0)))

#mean:返回数组中元素的算术平均值
num_np = np.array([[1,2,3],[3,4,5],[4,5,6]])
print('初始数组：\n{}'.format(num_np))
print('mean:\n{}'.format(np.mean(num_np)))
print('mean0列：\n{}'.format(np.mean(num_np,0)))

#average:根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值
num_np = np.array([1,2,3,4])
print('初始数组：\n{}'.format(num_np))
print('average:\n{}'.format(np.average(num_np)))
#不指定权重时相当于mean函数
wts = np.array([4,3,2,1])
print('权重average:\n{}'.format(np.average(num_np,weights=wts)))
#returned参数为True,返回权重的和
print('权重的和：\n{}'.format(np.average(num_np,weights=wts,returned=True)))
#多维数组中指定计算轴
num_np = np.arange(6).reshape(3,2)
print('初始数组：\n{}'.format(num_np))
wt = np.array([3,5])
print('多维数组1行：\n{}'.format(np.average(num_np,1,weights=wt)))

#std:标准差
print('标准差std:\n{}'.format(np.std([1,2,3,4])))

#var:方差
print('方差var:\n{}'.format(np.var([1,2,3,4])))