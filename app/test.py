#coding:utf8

import datetime
import time

d1 = datetime.datetime.now()
time.sleep(3)
d2 = datetime.datetime.now()
d = d2-d1      ### 产生的是 datetime.timedelta 对象

print d.days