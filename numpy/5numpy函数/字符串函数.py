import numpy as np

#add:对两个数组的逐个字符串元素进行连接
#multiply：返回按元素多重连接后的字符串
#center：居中字符串
#capitalize：将字符串的第一个字母转换为大写
#lower：将数组元素转换为小写
#upper：将数组元素转换为大写
#split：指定分隔符对字符串进行分割，并返回数组列表
#splitlines：返回元素中的行列表，以换行符分割
#strip：移除元素开头或结尾处的特定字符
#join：通过指定分隔符连接数组中的元素
#replace：使用新字符串替换字符串中的所有子字符串
#encode：数组元素依次调用str.encode
#decode：数组元素依次调用str.decode

#add:对两个数组的逐个字符串元素进行连接
print('两个字符串连接：\n{}'.format(np.char.add(['hello'],['world'])))
print('连接示例：\n{}'.format(np.char.add(['中国','欢迎'],['你好','你'])))

#multiply：返回按元素多重连接后的字符串
print('多重连接：\n{}'.format(np.char.multiply('numpy ',3)))

#center：居中字符串
print('居中显示：\n{}'.format(np.char.center('numpy',20,fillchar='*')))

#capitalize：将字符串的第一个字母转换为大写
print('第一个字母转换成大写：\n{}'.format(np.char.capitalize('numpy')))

#split：指定分隔符对字符串进行分割，并返回数组列表
print('每一个单词的第一个字母转化为大写：\n{}'.format(np.char.title('i like python')))

#lower：将数组元素转换为小写
print('所有字母转化为小写：\n{}'.format(np.char.lower(['NUMPY','PANDAS'])))

#upper：将数组元素转换为大写
print('所有字母转化为大写：\n{}'.format(np.char.upper(['numpy','pandas'])))

#split：指定分隔符对字符串进行分割，并返回数组列表,默认分隔符为空格
print('指定分隔符分割字符串：\n{}'.format(np.char.split('www.python.org',sep='.')))

#splitlines：返回元素中的行列表，以换行符分割
print('以换行符为分隔符分割字符串：\n{}'.format(np.char.splitlines('i\nlike\npython')))

#strip：移除元素开头或结尾处的特定字符,移除字符串头尾的指定字符,有多个也移除，可数组元素
print('移除字符串头尾的指定字符: \n{}'.format(np.char.strip('hHello worldhh','h')))

#join：通过指定分隔符连接数组中的元素,指定多个分隔符操作数组元素
print('指定多个分隔符操作数组元素: \n{}'.format(np.char.join([':','-'],['numpy','pandas'])))

#replace：使用新字符串替换字符串中的所有子字符串
print('替换字符：\n{}'.format(np.char.replace('how do you do','o','O')))

#encode：数组元素依次调用str.encode
print('字符串numpy编码后：\n{}'.format(np.char.encode('numpy','cp500')))

#decode：数组元素依次调用str.decode
str_v = np.char.encode('numpy','cp500')
print('解码前：\n{}'.format(str_v))
print('解码后：\n{}'.format(np.char.decode(str_v,'cp500')))