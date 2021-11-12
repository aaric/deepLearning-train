"""
函数示例

@author Aaric
@version 0.3.0-SNAPSHOT
"""


# 基于元组的可变参数（*可变参数）
def add(*numbers):
    total = 0.0
    for num in numbers:
        total += num
    return total


# print
print("{}".format(add(1.0, 2.0, 3.0)))


# 基于字典的可变参数（**可变参数）
def show_info(**info):
    for key, value in info.items():
        print("{0} - {1}".format(key, value))


# print
show_info(name="Kitty", age=18, sex=True)


# 函数对象-加法
def add(m, n):
    return m + n


# 函数对象-减法
def subtract(m, n):
    return m - n


# 函数对象-函数对象
def calc(opr):
    if "+" == opr:
        return add
    else:
        return subtract


# print
print("{0} + {1} = {2}".format(2, 1, calc("+")(2, 1)))
print("{0} - {1} = {2}".format(2, 1, calc("-")(2, 1)))


# 函数对象-lambda
def calc2(opr):
    if "+" == opr:
        return lambda m, n: m + n
    else:
        return lambda m, n: m - n


# print
print("{0} + {1} = {2}".format(2, 1, calc2("+")(2, 1)))
print("{0} - {1} = {2}".format(2, 1, calc2("-")(2, 1)))

# 函数对象-zip
arr1 = [1, 2, 3]
arr2 = ["cat", "dog", "pig", "tiger"]
arr3 = zip(arr1, arr2)
for obj in arr3:
    print(obj)
