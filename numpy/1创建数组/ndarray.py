import numpy as np


nd_one = np.arange(12)
#ndim返回数组维度
print('数组的维度：{}'.format(nd_one.ndim))

nd_sh = np.array([[1,2,3], [4,5,6]])
#shape表示数组的维度、调整数组的大小
print('数组的维度：{}'.format(nd_sh.shape))
nd_sh.shape = (3,2)
print('调整后的数组：{}'.format(nd_sh))