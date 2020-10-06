import time
# 装饰器=高阶函数+嵌套函数
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('test1 run time is %s'%(end_time-start_time))
    return wrapper

@timer    #等价于 test1 = timer(test1)
def test1():
    time.sleep(3)
    print('in the test1:')

test1()