import time
# 装饰器=高阶函数+嵌套函数
def timer(func):
    def wrapper(*args):
        start_time = time.time()
        func(args)
        end_time = time.time()
        print('test1 run time is %s'%(end_time-start_time))
    return wrapper

@timer    #等价于 test1 = timer(test1)
def test1(name):
    time.sleep(3)
    print('in the test1:',name)

test1('Louis')
"""
如果test1函数在定义时有参数，我们还像之前那样调用test1(name)，报错
TypeError: wrapper() takes 0 positional arguments but 1 was given
根据报错信息，可以推算出wrapper需要定义接收位置参数，将wrapper中添加可变参数
func()函数中没有加入参数又报如下错误，在func(args)
TypeError: test1() missing 1 required positional argument: 'name'
"""
