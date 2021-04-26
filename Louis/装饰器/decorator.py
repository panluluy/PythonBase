import time
"""
装饰器的作用就是在不修改被装饰对象源代码和调用方式的前提下为被装饰对象添加额外的功能
"""

def test1():
    time.sleep(3)
    print('in the test1')

def test2(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print('test1 run time is %s'%(end_time-start_time))

test1 = test2(test1)