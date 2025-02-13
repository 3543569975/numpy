import numpy as np


x_np = np.array([[1],[2],[3]])
y_np = np.array([4,5,6])

#将x_np与y_np相加

#flat函数
b_np = np.broadcast(x_np,y_np)
c = np.empty(b_np.shape)
c.flat = [i+k for (i,k) in b_np]
print('flat函数数组相加：\n{}'.format(c))

#直接相加
print('直接相加：\n{}'.format(x_np+y_np))
