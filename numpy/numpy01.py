"""
NumPy - 基本操作

@author Aaric
@version 0.4.0-SNAPSHOT
"""
import numpy as np

# 创建矩阵
arr1 = np.array([[1, 5, 3],
                 [2, 6, 4]])
print(arr1)

# 维度
print(arr1.ndim)

# 形状
print(arr1.shape)

# 大小
print(arr1.size)

# 元素类型
print(arr1.dtype)

# 索引
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

# 浅拷贝（共享一块内存）
arr2 = arr1
print(arr2)

# 深拷贝
arr3 = arr1.copy()
print(arr3)
