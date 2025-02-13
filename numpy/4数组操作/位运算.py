import numpy as  np

#bitwise_and:对数组执行位与操作
#bitwise_or:对数组元素执行位或操作
#invert:按位取反
#left_shift:向左移动二进制表示的位
#right_shift:向右移动二进制表示的位

#bitwise_and:对数组执行位与操作
#111,100,010,000
print('13和17的二进制形式：{}，{}'.format(bin(13),bin(17)))
print('13和17的位与：{}'.format(np.bitwise_and(13,17)))

#bitwise_or:对数组元素执行位或操作
#111,101,011,000
print('13和17的二进制形式：{}，{}'.format(bin(13),bin(17)))
print('13和17的位与：{}'.format(np.bitwise_or(13,17)))

#invert:按位取反
num_np = np.invert(np.array([13],dtype=np.uint8))
print('13的位反转，其中ndarray的dtype是uint8：{}'.format(num_np))
num_13_bin = np.binary_repr(13,width=8)
print('13的二进制表示：{}'.format(num_13_bin))
num_242_bin = np.binary_repr(242,width=8)
print('242的二进制表示：{}'.format(num_242_bin))

#left_shift:向左移动二进制表示的位
print('将5左移两位：{}'.format(np.left_shift(5,2)))
print('5的二进制表示：{}'.format(np.binary_repr(5,width=8)))
print('20的二进制表示：{}'.format(np.binary_repr(20,width=8)))

#right_shift:向右移动二进制表示的位
print('将20右移两位：{}'.format(np.right_shift(20,2)))
print('20的二进制表示：{}'.format(np.binary_repr(20,width=8)))
print('5的二进制表示：{}'.format(np.binary_repr(5,width=8)))