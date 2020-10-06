__author__ = 'Louis-Pan'

import time

# 返回当前时间的时间戳
print(time.time())

# 元祖形式返回当前时间
print(time.localtime())

# 格式化时间输出，[格式化，元祖时间]
print(time.strftime("%Y-%m-%d %X",time.localtime()))

# 返回当前时间的秒，后接元祖形式；以1970-01-01开始计算
print(time.mktime(time.localtime()))

# 返回星期，月，日，时间，年
print(time.ctime())