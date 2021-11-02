"""
NumPy - 分割

@author Aaric
@version 0.4.0-SNAPSHOT
"""
import numpy as np

# 水平分割
arr1 = np.arange(12).reshape(3, 4)
print(arr1)
arr2, arr3 = np.split(arr1, 2, axis=1)
print(arr2)
print(arr3)
arr2, arr3 = np.hsplit(arr1, 2)
print(arr2)
print(arr3)

# 垂直分割
arr4, arr5, arr6 = np.split(arr1, 3, axis=0)
print(arr4)
print(arr5)
print(arr6)
arr4, arr5, arr6 = np.vsplit(arr1, 3)
print(arr4)
print(arr5)
print(arr6)
