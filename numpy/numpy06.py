"""
NumPy - 概念

@author Aaric
@version 0.4.0-SNAPSHOT
"""
import numpy as np

# 标量（标量张量、零维张量、0D张量） -> 0轴或0阶
arr1 = np.array(10)
print(arr1.ndim)

# 向量（一维张量、1D张量）
# 3个元素叫3D向量，5个元素叫5D向量 -> 1轴或1阶
arr2 = np.array([10, 20, 30])
print(arr2.ndim)

# 矩阵（二维张量、2D张量） -> 2轴或2阶
arr3 = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])
print(arr3.ndim)

# 3D张量或更高维张量
arr4 = np.array([[[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]],
                 [[11, 21, 31],
                  [41, 51, 61],
                  [71, 81, 91]],
                 [[12, 22, 32],
                  [42, 52, 62],
                  [72, 82, 92]]])
print(arr4.ndim)
