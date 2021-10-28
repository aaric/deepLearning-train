"""
NumPy - 矩阵运算

@author Aaric
@version 0.4.0-SNAPSHOT
"""
import numpy as np

# 创建矩阵
arr1 = np.array([[3, 3, 3],
                 [3, 3, 3]])
arr2 = np.array([[2, 2, 2],
                 [2, 2, 2]])

# 简单加法
print(arr1 + arr2)

# 简单减法
print(arr1 - arr2)

# 简单乘法
print(arr1 * arr2)
print(arr1 * 3)

# 简单N次方
print(arr1 ** arr2)

# 简单除法
print(arr1 / arr2)
print(arr1 // arr2)

# 简单取模
print(arr1 % arr2)

# 简单bool
print(arr1 > 3)

# 转置矩阵
arr3 = arr2.T
print(arr3)
print(np.transpose(arr2))

# 矩阵乘法
print(arr1.dot(arr3))
