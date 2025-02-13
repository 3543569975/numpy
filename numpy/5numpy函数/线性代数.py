import numpy as np


#dot:两个数组的点积，元素对应相乘
np1 = np.array([[1,2],[3,4]])
np2 = np.array([[11,12],[13,14]])
print(np.dot(np1,np2))
#计算方法：[[1*11+2*13，1*12+2*14],[3*11+4*13,3*12+4*14]]

#vdot:两个向量的点积
np1 = np.array([[1,2],[3,4]])
np2 = np.array([[11,12],[13,14]])
print('vdot:\n{}'.format(np.vdot(np1,np2)))
#1*11+2*12+3*13+4*14

#inner:返回一维数组的向量内积
np1 = np.array([1,2,3])
np2 = np.array([0,1,0])
print('inner:\n{}'.format(np.inner(np1,np2)))
#1*0+2*1+3*0
#多维数组
np1 = np.array([[1,2],[3,4]])
np2 = np.array([[11,12],[13,14]])
print('inner（多维数组）:\n{}'.format(np.inner(np1,np2)))
#[[1*11+2*12,1*13+2*14],[3*11+4*12,3*13+4*14]]

#matmul:返回两个数组的矩阵乘积
np1 = [[1,0],[0,1]]
np2 = [[4,1],[2,2]]
print('matmul（矩阵乘积）:\n{}'.format(np.matmul(np1,np2)))
np1 = np.arange(8).reshape(2,2,2)
np2 = np.arange(4).reshape(2,2)
print('多维矩阵乘积：\n{}'.format(np.matmul(np1,np2)))

#linalg.det:计算输入矩阵的行列式
np1 = np.array([[1,2],[3,4]])
print('np1的行列式：{}'.format(np.linalg.det(np1)))
np2 = np.array([[6,1,1],[4,-2,5],[2,8,7]])
print('np2的行列式：{}'.format(np.linalg.det(np2)))
#行列式计算公式
#6*（-2*7-5*8）-1*（4*7-5*2）+1*（4*8--2*2）

#linalg.solve:给出矩阵形式的线性方程的解([3,5])
np1 = [[2,3],[3,2]]
np2 = [21,19]
print(np.linalg.solve(np1,np2))

#linalg.inv:计算矩阵的乘法逆矩阵
np1 = np.array([[1,2],[3,4]])
np1_inv = np.linalg.inv(np1)
print('np2:\n{}'.format(np1_inv))
print('np1,np2的点积：\n{}'.format(np.dot(np1,np1_inv)))
np2 = np.array([[1,1,1],[0,2,5],[2,5,-1]])
print('np2:\n{}'.format(np2))
np2_inv = np.linalg.inv(np2)
print('np2的逆矩阵：\n{}'.format(np2_inv))
np3 = [[6],[-4],[27]]
solve_ = np.linalg.solve(np2,np3)
print('计算：a^(-1)b:\n{}'.format(solve_))