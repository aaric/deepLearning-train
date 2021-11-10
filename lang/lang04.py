"""
日期与时间示例

@author Aaric
@version 0.5.0-SNAPSHOT
"""

import datetime
import time

from pytz import timezone

# 当前时间
c1 = datetime.datetime.today()
c2 = datetime.datetime.now(tz=timezone("Asia/Shanghai"))
print(c1)
print(c2)

# 加减时间
c1 += datetime.timedelta(10)
c2 += datetime.timedelta(weeks=-5)
print(c1)
print(c2)

# 获取时间秒
ts1 = datetime.datetime.now().timestamp()
ts2 = time.mktime(c1.timetuple())
print(int(ts1))
print(int(ts2))

# 转换秒时间为datetime
d1 = datetime.datetime.fromtimestamp(ts1, tz=timezone("Asia/Shanghai"))
print(d1)
