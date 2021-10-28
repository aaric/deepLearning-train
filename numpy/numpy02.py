"""
NumPy - 创建矩阵

@author Aaric
@version 0.4.0-SNAPSHOT
"""
import numpy as np

# 二维矩阵
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(arr1)

# 全0矩阵
arr2 = np.zeros((2, 3))
print(arr2)

# 全1矩阵
arr3 = np.ones((2, 3))
print(arr3)

# 空值矩阵（接近于0）
arr4 = np.empty((2, 3))
print(arr4)

# 范围矩阵
arr5 = np.arange(10)
arr6 = np.arange(5, 15)
arr7 = np.arange(5, 15, 3)
arr8 = np.arange(12).reshape(3, 4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
