import numpy as np


#np.ravel(a,order = 'c')
#order:'c'为行方向，'f'为列方向，'A'为任意方向（默认），'k'为元素在内存中的出现顺序
num_np = np.arange(8).reshape(2,4)
print('原始数组：  \n{}'.format(num_np))
print('调用ravel函数之后：\n{}'.format(num_np.ravel()))
print('以Fortran语言风格顺序调用ravel函数之后：\n{}'.format(num_np.ravel(order='F')))