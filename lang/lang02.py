"""
算法示例

@author Aaric
@version 0.3.0-SNAPSHOT
"""

# 1232345123 -> 123 2345 123
idx = [0]
arr = [1, 2, 3, 2, 3, 4, 5, 1, 2, 3]
for i in range(0, len(arr) - 1):
    if arr[i] > arr[i + 1]:
        idx.append(i + 1)
idx.append(len(arr))

for i in range(0, len(idx) - 1):
    m = idx[i]
    n = idx[i + 1]
    print(arr[m:n])

# array extend
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr1.extend(arr2)
print(arr1)

# array filter
arr3 = [4, 5, 6]


def f1(x):
    return x > 5


arr4 = list(filter(f1, arr3))
print(arr4)
arr4 = list(filter(lambda x: x > 5, arr3))
print(arr4)

# arr map
arr5 = [1, 2, 3]


def f2(x):
    return x ** 2


arr6 = list(map(f2, arr5))
print(arr6)
arr6 = list(map(lambda x: x ** 2, arr5))
print(arr6)
