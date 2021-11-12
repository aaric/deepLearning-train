"""
文件示例

@author Aaric
@version 0.5.0-SNAPSHOT
"""

filename = "../requirements.txt"
file = None

# 方法一
try:
    file = open(filename)
    content = file.read()
    print("content: {0}".format(content))
except FileNotFoundError as e:
    print("except: no such file or directory")
except UnicodeDecodeError as e:
    print("except: illegal multibyte sequence")
except OSError as e:
    print("except: os error")
finally:
    if file is not None:
        file.close()

# 方法二
with open(filename) as file:
    content = file.read()
    print("content: {0}".format(content))
