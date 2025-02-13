import numpy as np


#sort:
num_np = np.array([[3,7],[9,1]])
print('初始数组：\n{}'.format(num_np))
print('sort:\n{}'.format(np.sort(num_np)))
print('sort0列：\n{}'.format(np.sort(num_np,0)))
#在sort中自定义排序字段
dt = np.dtype([('name','S10'),('age',int)])
num_np = np.array([('meng',21),('zhi',25),('li',17),('zhang',27)],dtype=dt)
print('初始数组：\n{}'.format(num_np))
print('按name排序：\n{}'.format(np.sort(num_np,order='name')))

#argsort:返回数组值从小到大的索引值
x_np = np.array([3,1,2])
print('初始数组：{}'.format(x_np))
y_np = np.argsort(x_np)
print('argsort:\n{}'.format(y_np))
print('以排序后的顺序重构原数组：\n{}'.format(x_np[y_np]))

#lexsort:对多个序列进行排序
name = ('meng','li','zhang','wang')
dv = ('f.y','s.y.','s.y.','f.y.')
lex_sort = np.lexsort((dv,name))
print('sort:\n{}'.format(lex_sort))
sort_rt = [name[i]+','+dv[i]for i in lex_sort]
print('使用索引获取排序后的数据：{}'.format(sort_rt))

#argmax:沿指定轴返回最大元素
num_np = np.array([[30,40,70],[80,20,10],[50,90,60]])
print('初始数组：\n{}'.format(num_np))
print('argmax:\n{}'.format(np.argmax(num_np)))
print('展开数组：{}'.format(num_np.flatten()))
max_index = np.argmax(num_np,axis=0)
print('沿轴0的最大值的索引值：{}'.format(max_index))

#argmin:沿指定轴返回最小元素
min_index = np.argmin(num_np)
print('argmin:{}'.format(min_index))
print('展开数组中的最小值：{}'.format(num_np.flatten()[min_index]))
min_index = np.argmin(num_np,0)
print('沿轴0的最小值索引：{}'.format(min_index))

#nonzero:返回输入数组中非零元素的索引
num_np = np.array([[30,40,0],[0,20,10],[50,0,60]])
print('初始数组：\n{}'.format(num_np))
print('nonzero:\n{}'.format(np.nonzero(num_np)))

#where:返回输入数组中满足给定条件的元素的索引
x_np = np.arange(9.).reshape(3,3)
print('初始数组:\n{}'.format(x_np))
y_np = np.where(x_np>3)
print('大于三的元素索引：\n{}'.format(y_np))
print('使用索引获取满足条件的元素：{}'.format(x_np[y_np]))

#extract:根据某个条件从数组中抽取元素，然后返回满足条件的元素
num_np = np.arange(9.).reshape(3,3)
print('初始数组:\n{}'.format(x_np))
#定义条件，选择偶数元素
condition = np.mod(num_np,2)==0
print('按元素的条件值：\n{}'.format(condition))
print('使用条件提取元素：{}'.format(np.extract(condition,num_np)))

#复数排序
print('复数排序：\n{}'.format(np.sort_complex([5,3,6,2,1])))
print('复数排序：\n{}'.format(np.sort_complex([1+2j,2-1j,3-2j,3-3j,3+5j])))

#分区排序
num_np = np.array([3,4,2,1])
#将数组中所有元素从小到大排序，比3小的放在前面，大的放在后面
print('分区排序：\n{}'.format(np.partition(num_np,3)))
#小于1的在前面，大于3的在后面，1和3之间的在中间
print('分区排序：\n{}'.format(np.partition(num_np,(1,3))))
#找到数组中第三小的值
print('第三小的值:\n{}'.format(num_np[np.argpartition(num_np,2)[2]]))
#同时找到第3小和第4小的值，用[2,3]同时将第3小和第4小的值排序，然后可以分别通过下标[2]和[3]获取
print('同时找到第3小和第4小的值，用[2,3]同时将第3小和第4小的值排序，然后可以分别通过下标[2]和[3]获取')
print('获取第3小的值:\n{}'.format(num_np[np.argpartition(num_np,[2,3])[2]]))
print('获取第4小的值:\n{}'.format(num_np[np.argpartition(num_np,[2,3])[3]]))
