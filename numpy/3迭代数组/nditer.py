import numpy as np

np_ar = np.arange(0,60,5)
np_ar = np_ar.reshape(3,4)
print('原始数组：  {}'.format(np_ar))

print('c语言风格排序：')
for i in np.nditer(np_ar,order = 'C'):
    print(i,end = ',')
print('\n')

print('以Fortran语言风格顺序排序：')
for i in np.nditer(np_ar,order = 'F'):
    print(i,end = ',')
print('\n')


print('原始数组：  \n{}'.format(np_ar))
#对元素值修改（X2）
for i in np.nditer(np_ar,op_flags = ['readwrite']):
    i[...] = 2*i

print('原始数组x2：\n{}'.format(np_ar))
print('\n')


#对每列进行遍历，并组合为一维数组
#c_index:可以跟踪c语言顺序索引
#f_index:可以跟踪Fortran语言顺序索引
#multi-index:每次迭代可以跟踪一种索引类型
#external_loop:给出的值是具有多个值的一维数组，而不是零维数组
np_ar = np.arange(0,60,5)
np_ar = np_ar.reshape(3,4)
print('原始数组：  {}'.format(np_ar))

print('对每列进行遍历，并组合为一维数组后的数组：')
for i in np.nditer(np_ar,flags = ['external_loop'],order = 'F'):
    print(i,end = ',')
print('\n')


#广播（对于不同形状的数组进行的数值计算的方法
np1_ar = np.arange(0,60,5)
np1_ar = np_ar.reshape(3,4)
print('数组1：  {}'.format(np1_ar))
np2_ar = np.array([1,2,3,4],dtype = int)
print('数组2：  {}'.format(np2_ar))

print('数组1：数组2：')
for x,y in np.nditer([np1_ar,np2_ar]):
    print('%d:%d'%(x,y),end = ',  ')
    #print(x+y,end = ',')