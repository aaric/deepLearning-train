"""
NumPy - 内置属性

@author Aaric
@version 0.4.0-SNAPSHOT
"""
import numpy as np

# 创建矩阵
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print(arr1)

# 维度
print(arr1.ndim)

# 形状
print(arr1.shape)

# 大小
print(arr1.size)

# 元素类型
print(arr1.dtype)
