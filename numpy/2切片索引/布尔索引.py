import numpy as np

np_ar = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print('初始数组：  {}'.format(np_ar))

#获取初始数组中大于5的元素
bg_5 = np_ar[np_ar > 5]
print('初始数组中大于5的元素：  {}'.format(bg_5))

#过滤非复数元素
#取补集（~），np_ar[~np.iscomplex(np_ar)]
np_ar = np.array([1,2+6j,5,0.1,3.5+5j])
print('初始数组：  {}'.format(np_ar))

filter_nr = np_ar[np.iscomplex(np_ar)]
print('过滤的非复数：  {}'.format(filter_nr))