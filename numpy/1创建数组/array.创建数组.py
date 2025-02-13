import numpy as np

#数组
np.array([1,2,3,4,5])
#元组
np.array((1,2,3,4,5))
#指定参数类型为复数
co_list = [1,2,3]
dy_np = np.array(co_list, dtype=complex, order='K')
print(dy_np)
#迭代对象
np.array(range(10))
#生成器
a = np.array(i**2 for i in range(10))
print(a)