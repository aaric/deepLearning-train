"""
日期与时间示例

@author Aaric
@version 0.4.0-SNAPSHOT
"""

import time
from datetime import datetime

from pytz import timezone

# 当前时间
c1 = datetime.today()
c2 = datetime.now(tz=timezone("Asia/Shanghai"))
print(c1)
print(c2)

# 获取时间秒
ts1 = datetime.now().timestamp()
ts2 = time.mktime(datetime.now().timetuple())
print(int(ts1))
print(int(ts2))

# 转换秒时间为datetime
d1 = datetime.fromtimestamp(ts1, tz=timezone("Asia/Shanghai"))
print(d1)
