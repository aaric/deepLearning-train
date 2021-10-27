# coding=utf-8

import datetime
import time

# 获取秒时间
print("{0}".format(int(datetime.datetime.now().timestamp())))
print("{0}".format(int(time.mktime(datetime.datetime.now().timetuple()))))

# 1232345123 -> 123 2345 123
idx = [0]
arr = [1, 2, 3, 2, 3, 4, 5, 1, 2, 3]
for i in range(0, len(arr) - 1):
    if arr[i] > arr[i+1]:
        idx.append(i + 1)
idx.append(len(arr))

for i in range(0, len(idx) - 1):
    m = idx[i]
    n = idx[i+1]
    print(arr[m:n])

# array extend
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr1.extend(arr2)
print(arr1)
