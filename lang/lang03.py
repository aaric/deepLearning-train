"""
异常示例

@author Aaric
@version 0.4.0-SNAPSHOT
"""

# 捕获异常
try:
    m = 100
    n = input("Input number: ")
    result = m / int(n)
    print("{0} % {1} = {2}".format(m, n, result))
except ZeroDivisionError as e:
    print("ZeroDivisionError: {0}".format(e))
except ValueError as e:
    print("ValueError: {0}".format(e))


# 自定义异常
class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


try:
    m = 100
    n = input("Input number: ")
    result = m / int(n)
    print("{0} % {1} = {2}".format(m, n, result))
except (ZeroDivisionError, ValueError) as e:
    print("{0}".format(e))
finally:
    raise CustomException("自定义异常")
