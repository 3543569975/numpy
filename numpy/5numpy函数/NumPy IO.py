import numpy as np


#save:保存文件数组数组数据、图形、dtype等
a = np.array([1,2,3,4,5])
np.save('outfile.npy',a)

#load:读取
b = np.load('outfile.npy')
print(b)

#savez:保存多个数组
a =  np.array([[1,2,3],[4,5,6]])
b = np.arange(0,1,0.1)
c = np.sin(b)
np.savez('numpy.npz',a,b,sin_array = c)
r = np.load('numpy.npz')
print(r.files)
print(r['arr_0'])
print(r['arr_1'])
print(r['sin_array'])