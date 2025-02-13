import numpy as np

#np.asarray(a,dtype = None, order = None)
# a = 任意形式的输入参数，列表// ， dtype=数据类型(int/float/)， order= ’c‘/’f'
#列表(元组/元组列表)转换为ndarry
num_list = [1,2,3]

list_to_nd = np.asarray(num_list)
print('np.asarray:  {}'.format(list_to_nd))


#np.frombuffer(buffer,dtype = float,count = -1,offest = 0)
#buffer=任意对象，dtype=数据类型(int/float/)，count=读取数据的数量，默认-1（所有），offest=读取的起始位置，默认0
pri_str = b'Hello World'
fb_np = np.frombuffer(pri_str,dtype='S1')
print('np.frombuffer:  {}'.format(fb_np))


#np.fromiter(iterable,dtype,count = -1)
#iterable=可迭代的对象，dtype=数据类型(int/float/)，count=读取数据的数量，默认-1（所有）
num_list = range(5)
iter_obj = iter(num_list)
nd_int = np.fromiter(iter_obj,dtype=int)
print('np.fromiter:  {}'.format(nd_int))


#np.arange(start,stop,step,dtype)
#start=起始值，默认0，stop=终止值（不包含），step=步长，dtype=数据类型(int/float/)
ar_np = np.arange(5,dtype=float)
print('np.arange:  {}'.format(ar_np))

#np.linspace(start,stop,num=50,endpoint=True,retstep=False,dtype=None)
#start=序列的起始值，stop=序列终止值，num=要生成的等步长的样本数量，默认50，endpoint=True(包含终止值），默认True
# retstep=Ture（显示间距）,默认False，dtype=数据类型(int/float/)默认float
df_np = np.linspace(1,10,10,endpoint=False,retstep=True)
print('np.linspace:  {}'.format(df_np))


#np.logspace(start,stop,num = 50,endpoint=True,base = 10.0,dtype=None)
#start=序列的起始值（base**start)，stop=序列终止值(base**stop)，num=要生成的等步长的样本数量，默认50，
#endpoint=True(包含终止值），默认True，base= 对数log的底数，参数表示取对数时log的下标,默认10,
# dtype=数据类型(int/float/)默认float
log_np = np.logspace(1,2,num=10,dtype=int)
print('np.logspace:  {}'.format(log_np))


