import numpy as np

#concatenate:连接沿现有轴的数组序列
#stack:沿新轴连接数组序列
#hstack:水平堆叠序列中的数组（列方向）
#vstack:垂直堆叠序列中的数组（行方向）


np1 = np.array([[1,2],[3,4]])
print('第一个数组：\n{}'.format(np1))
np2 = np.array(([5,6],[7,8]))
print('第二个数组：\n{}'.format(np2))

#两个数组的维度一样
#concatenate:连接沿现有轴的数组序列
print('沿轴0连接两个数组：\n{}'.format(np.concatenate((np1,np2))))
print('沿轴1连接两个数组：\n{}'.format(np.concatenate((np1,np2),axis=1)))

#stack:沿新轴连接数组序列
print('沿轴0连接两个数组：\n{}'.format(np.stack((np1,np2),0)))
print('沿轴1连接两个数组：\n{}'.format(np.concatenate((np1,np2),1)))

#hstack:水平堆叠序列中的数组（列方向）
print('水平堆叠：\n{}'.format(np.hstack((np1,np2))))

#vstack:垂直堆叠序列中的数组（行方向）
print('垂直堆叠：\n{}'.format(np.vstack((np1,np2))))