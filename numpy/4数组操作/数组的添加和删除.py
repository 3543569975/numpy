import numpy as np

#resize:返回指定大小的新数组
#append:将值添加到数组末尾
#insert:沿指定轴将值插入指定下标之前
#unique:查找数组内的唯一元素

np1 = np.array([[1,2,3],[4,5,6]])

print('第一个数组：\n{}'.format(np1))
print('第一个数组的形状：\n{}'.format(np1.shape))

np2 = np.resize(np1,(3,2))
print('第二个数组：\n{}'.format(np2))
print('第二个数组的形状：\n{}'.format(np2.shape))

np2 = np.resize(np1,(3,3))
print('第二个数组修改大小后：\n{}'.format(np2))

#append:将值添加到数组末尾
num_np = np.array([[1,2,3],[4,5,6]])
print('初始数组：\n{}'.format(num_np))
print('向数组添加元素[7,8,9]：\n{}'.format(np.append(num_np,[7,8,9])))
print('沿轴0添加元素[7,8,9]：\n{}'.format((np.append(num_np,[[7,8,9]],axis=0))))
print('沿轴1添加元素[7,8,9]：\n{}'.format(np.append(num_np,[[5,5,5],[7,8,9]],axis = 1)))

#insert:沿指定轴将值插入指定下标之前
num_np = np.array([[1,2],[3,4],[5,6]])
print('初始数组：\n{}'.format(num_np))
print('未传递axis参数，在插入之前输入数组会被展开：')
print(np.insert(num_np,3,[11,12]))

print('传递了axis参数，会广播数组来配输入数组')
print('沿轴0广播:\n{}'.format(np.insert(num_np,1,[11],axis=0)))
print('沿轴1广播：\n{}'.format(np.insert(num_np,1,[11],axis=1)))

#delete(arr,obj,axis):a返回从输入数组中删除指定子数组的新数组
num_np = np.arange(12).reshape(3,4)
print('初始数组：\n{}'.format(num_np))
print('未传递axis参数，在插入之前输入数组会被展开：')
print(np.delete(num_np,5))

print('删除第二列：\n{}'.format(np.delete(num_np,1,axis=1)))

print('包含从数组中删除的替代值的切片：')
num_np = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.delete(num_np,np.s_[::2]))

#unique:查找数组内的唯一元素
num_np = np.array([5,2,6,2,7,5,6,8,2,9])
print('初始数组：\n{}'.format(num_np))

unique_np = np.unique(num_np)
print('数组去重：\n{}'.format(unique_np))

print('去重数组的索引数组：')
unique_np,indices = np.unique(num_np,return_index=True)
print(indices)

print('每个和原数组下标对应的数值：')
print(num_np)

print('去重数组的下标：')
unique_np,indices = np.unique(num_np,return_inverse=True)
print(unique_np)
print('下标为：\n{}'.format(indices))

print('使用下标重构原数组：')
print(unique_np[indices])

print('返回去重元素的重复数量：')
unique_np,indices = np.unique(num_np,return_counts=True)
print(unique_np)
print(indices)