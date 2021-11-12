"""
多线程示例

@author Aaric
@version 0.5.0-SNAPSHOT
"""

# 线程函数
import time
from threading import Thread, current_thread


def thread_body():
    t = current_thread()
    for i in range(5):
        print("{0} - {1}".format(i, t.getName()))
        time.sleep(1)
    print("{0} over!".format(t.getName()))


t1 = Thread(target=thread_body)
t2 = Thread(target=thread_body, name="T2")
t1.start()
t2.start()


# 自定义线程类
class CustomThread(Thread):
    def __init__(self, name=None):
        super().__init__(name=name)

    def run(self):
        t = current_thread()
        for i in range(5):
            print("{0} - {1}".format(i, t.getName()))
            time.sleep(1)
        print("{0} over!".format(t.getName()))


t3 = CustomThread("T3")
t3.start()
