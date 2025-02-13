import numpy as np

angle_num = np.array([0,30,45,60,90])
print('数组中各个角度的正弦值：')
#通过乘pi/180转化弧度
print(np.sin(angle_num*np.pi/180))

print('数组中各个角度的余弦值：')
print(np.cos(angle_num*np.pi/180))

print('数组中各个角度的正切值：')
print(np.tan(angle_num*np.pi/180))

#反三角函数
print('数组中各个角度的正弦值：')
print(np.sin(angle_num*np.pi/180))
print('各个角度的反正弦，返回值以弧度为单位：\n{}'.format(np.arcsin(np.sin(angle_num*np.pi/180))))

print('数组中各个角度的余弦值：')
print(np.cos(angle_num*np.pi/180))
print('各个角度的反余弦，返回值以弧度为单位：\n{}'.format(np.arccos(np.cos(angle_num*np.pi/180))))

print('数组中各个角度的正切值：')
print(np.tan(angle_num*np.pi/180))
print('各个角度的反正切，返回值以弧度为单位：\n{}'.format(np.arctan(np.tan(angle_num*np.pi/180))))

print('各个角度的角度制单位：\n{}'.format(np.degrees(np.arctan(np.tan(angle_num*np.pi/180)))))


#舍入函数
num_py = np.array([0.5,1.0,2.55,13.321,67.567,125.132,357.72,55])

print('原始数组:\n{}'.format(num_py))
print('正常舍入：\n{}'.format(np.around(num_py)))
print('舍入一位小数：\n{}'.format(np.around(num_py,decimals=1)))
print('舍入两位小数：\n{}'.format(np.around(num_py,decimals=2)))
print('舍入到十位：\n{}'.format(np.around(num_py,decimals=-1)))
print('舍入到百位：\n{}'.format(np.around(num_py,decimals=-2)))

#floor:返回数字的下舍整数
num_py = np.array([-11.7,3.6,-1.2,0.32,6.3,10,218.29])
print('初始数组：\n{}'.format(num_py))
print('下舍后的数组：\n{}'.format(np.floor(num_py)))


#ceil:返回数字的上入整数
num_py = np.array([-11.7,3.6,-1.2,6.3,10,218.29])
print('初始数组：\n{}'.format(num_py))
print('上入后的数组：\n{}'.format(np.ceil(num_py)))

#算术函数
np1 = np.arange(9,dtype = np.float_).reshape(3,3)
print('第一个数组：\n{}'.format(np1))
np2 = np.array([10,10,10])
print('第二个数组：\n{}'.format(np2))
print('两个数组相加：\n{}'.format(np.add(np1,np2)))
print('两个数组相减：\n{}'.format(np.subtract(np1,np2)))
print('两个数组相乘：\n{}'.format(np.multiply(np1,np2)))
print('两个数组相除：\n{}'.format(np.divide(np1,np2)))
np3 = np.array([0.25,0.5,1.66,5,20,100])
print('第三个数组的倒数：\n{}'.format(np.reciprocal(np3)))

#power:将第一个输入数组中的元素作为底数，计算它与第二个输入数组中的对应元素的幂
np2 = np.array([10,100,1000])
print('power:\n{}'.format(np.power(np2,2)))
np3 = np.array([1,2,3])
print('power:\n{}'.format(np.power(np2,np3)))

#mod:计算输入数组中相应元素扣除后的余数。=remainder
np1 = np.array([10,25,50])
np2 = np.array([3,5,9])
print('第一个数组：\n{}'.format(np1))
print('第二个数组：\n{}'.format(np2))
print('mod:\n{}'.format(np.mod(np1,np2)))
print('remainder:\n{}'.format(np.remainder(np1,np2)))