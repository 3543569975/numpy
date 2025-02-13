import numpy as np

#对数组转置
num_np = np.arange(12).reshape(3,4)
print('原始数组：\n{}'.format(num_np))
print('转置数组：\n{}'.format((num_np.T)))