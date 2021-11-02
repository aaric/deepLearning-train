"""
NumPy - 合并

@author Aaric
@version 0.4.0-SNAPSHOT
"""
import numpy as np

# 合并
arr1 = np.array([[1, 5, 3],
                 [2, 6, 4]])
arr2 = np.array([[1, 1, 1],
                 [1, 1, 1]])
print(arr2.shape)
arr3 = np.stack((arr1, arr2), axis=0)
print(arr3)
print(arr3.shape)

# 水平合并
arr4 = np.hstack((arr1, arr2))
print(arr4)
print(arr4.shape)

# 垂直合并
arr5 = np.vstack((arr1, arr2))
print(arr5)
print(arr5.shape)

# 拼接：axis=0 -> vstack , axis=1 -> hstack
arr6 = np.concatenate((arr1, arr2), axis=1)
print(arr6)
print(arr6.shape)

# 新增维度
arr7 = np.array([1, 2, 3])
arr8 = arr7[np.newaxis, :]
print(arr8)
print(arr8.shape)
arr9 = arr7[:, np.newaxis]
print(arr9)
print(arr9.shape)
arr10 = arr9.T
print(arr10)
print(arr10.shape)
arr11 = np.atleast_2d(arr7)
print(arr11)
print(arr11.shape)
