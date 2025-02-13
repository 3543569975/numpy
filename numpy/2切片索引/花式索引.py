import numpy as np

np_ar =  np.arange(32).reshape((8,4))
print('初始数组：  {}'.format(np_ar))

#顺序索引（可倒序）
fancy_ar = np_ar[[4,2,1,7]]
print('顺序索引结果(第4，2，1，7行)：  \n{}'.format(fancy_ar))

#多个索引组
fancy_ar = np_ar[np.ix_([1,5,7,2],[0,3,1,2])]
print('多个索引组结果（第1，5，7，2行，0，3，1，2列：  \n{}'.format(fancy_ar))
