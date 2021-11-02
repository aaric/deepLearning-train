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
print(np.dot(arr1, arr3))

# 求和
arr4 = np.array([[1, 5, 3],
                 [2, 6, 4]])
print(np.sum(arr4))
print(np.sum(arr4, axis=0))
print(np.sum(arr4, axis=1))

# 求极值
print(np.min(arr4))
print(np.argmin(arr4))
print(np.max(arr4))
print(np.argmax(arr4))

# 求平均值
print(arr4.mean())
print(np.mean(arr4))

# 求中位数
print(np.median(arr4))

# 求开方
print(np.sqrt(arr4))

# 排序
print(np.sort(arr4))
print(np.argsort(arr4))

# 夹子
print(np.clip(arr4, 3, 4))
