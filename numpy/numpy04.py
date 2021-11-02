"""
NumPy - 矩阵运算

@author Aaric
@version 0.4.0-SNAPSHOT
"""
import numpy as np

# 索引
arr1 = np.array([[1, 5, 3],
                 [2, 6, 4]])
print(arr1.shape)
print(arr1[1][2])
print(arr1[1, 2])
print(arr1[:, 2])

# 迭代
for hi in arr1:
    print(hi)
for vi in arr1.T:
    print(vi)
for fi in arr1.flat:
    print(fi)

# 堆叠
arr2 = np.array([[1, 1, 1],
                 [1, 1, 1]])
print(arr2.shape)
arr3 = np.stack((arr1, arr2), axis=0)
print(arr3)
print(arr3.shape)

# 水平堆叠
arr4 = np.hstack((arr1, arr2))
print(arr4)
print(arr4.shape)

# 垂直堆叠
arr5 = np.vstack((arr1, arr2))
print(arr5)
print(arr5.shape)
