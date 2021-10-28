"""
函数

@author Aaric
@version 0.3.0-SNAPSHOT
"""


# 基于元组的可变参数（*可变参数）
def sum(*numbers):
    total = 0.0
    for num in numbers:
        total += num
    return total


print("{}".format(sum(1.0, 2.0, 3.0)))


# 基于字典的可变参数（**可变参数）
def show_info(**info):
    for key, value in info.items():
        print("{0} - {1}".format(key, value))


show_info(name="Kitty", age=18, sex=True)
