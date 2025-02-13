import numpy as np


#split:将一个数组分割为多个数组
#hsplit:将一个数组水平分割为多个子数组（按列）
#vsplit:将一个数组垂直分割为多个子数组（按行）


num_np = np.arange(9)
print('原始数组：\n{}'.format(num_np))

#split:将一个数组分割为多个数组
print('将一个数组分为三个大小相等的子数组：\n{}'.format(np.split(num_np,3)))
print('将一个数组在一维数组中表明的位置分割：\n{}'.format(np.split(num_np,[4,7])))

#hsplit:将一个数组水平分割为多个子数组（按列）
num_np = np.floor(10*np.random.random((2,6)))
print('原始数组：\n{}'.format(num_np))
print('水平分割后：\n{}'.format(np.hsplit(num_np,3)))

#vsplit:将一个数组垂直分割为多个子数组（按行）
num_np = np.arange(16).reshape(4,4)
print('原始数组：\n{}'.format(num_np))
print('垂直分割后：\n{}'.format(np.vsplit(num_np,2)))