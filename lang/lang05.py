"""
正则式示例

@author Aaric
@version 0.5.0-SNAPSHOT
"""

import re

# 匹配
p1 = r"^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
email = "aaric@github.com"
m1 = re.match(p1, email)
if m1 is not None:
    print(m1)

# 查找
p2 = r"java|Java|JAVA"
likes = "I like java and Java and JAVA."
print(re.findall(p2, likes))

# 替换
p3 = r"\d+"
text = "A01B02C03"
print(re.sub(p3, " ", text))
print(re.sub(p3, " ", text, 1))
