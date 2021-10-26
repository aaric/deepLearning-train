# coding=utf-8

import datetime
import time

# 获取秒时间
print("{0}".format(int(datetime.datetime.now().timestamp())))
print("{0}".format(int(time.mktime(datetime.datetime.now().timetuple()))))
