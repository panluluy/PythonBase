import time
# 装饰器=高阶函数+嵌套函数
def timer(func):
    def wrapper(name,*args,**kwargs):
        start_time = time.time()
        '''
        注意此处必须是*args和**kwargs，如果是args和kwargs，在传入test1函数时
        name传递给name，args和kwargs全部传递给*args
        '''
        func(name,*args,**kwargs)
        end_time = time.time()
        print('test1 run time is %s'%(end_time-start_time))
    return wrapper

@timer    #等价于 test1 = timer(test1)
def test1(name,*args,**kwargs):
    time.sleep(3)
    print('in the test1:',name,'===',args,'***',kwargs)

test1('Louis','18','Pan',sex='man',tel='123456')
"""
如果test1函数在定义时有参数，我们还像之前那样调用test1(name)，报错
TypeError: wrapper() takes 0 positional arguments but 1 was given
根据报错信息，可以推算出wrapper需要定义接收位置参数，将wrapper中添加可变参数
func()函数中没有加入参数又报如下错误，在func(args)
TypeError: test1() missing 1 required positional argument: 'name'
"""
