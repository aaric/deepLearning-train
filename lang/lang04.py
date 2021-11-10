"""
日期与时间示例

@author Aaric
@version 0.5.0-SNAPSHOT
"""

import time
from datetime import datetime
from datetime import timedelta

from pytz import timezone

# 当前时间
d1 = datetime.today()
d2 = datetime.now(tz=timezone("Asia/Shanghai"))
print("ds1={0}".format(d1))
print("ds2={0}".format(d2))

# 加减时间
d1 += timedelta(10)
d2 += timedelta(weeks=-5)
print("ds1={0}".format(d1))
print("ds2={0}".format(d2))

# 获取时间秒
ts1 = datetime.now().timestamp()
ts2 = time.mktime(d1.timetuple())
print("ts1={0}".format(int(ts1)))
print("ts2={0}".format(int(ts2)))

# 转换秒时间为datetime
d3 = datetime.fromtimestamp(ts1, tz=timezone("Asia/Shanghai"))
print("ds3={0}".format(d3))

# 格式化字符串
ds1 = "2021-12-12 12:00:00"
d4 = datetime.strptime(ds1, "%Y-%m-%d %H:%M:%S")
print("ds4={0}".format(d4))
ds2 = d4.strftime("%Y-%m-%d %H:%M:%S")
print("ds2={0}".format(ds2))
