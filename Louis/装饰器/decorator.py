import time

def test1():
    time.sleep(3)
    print('in the test1')

def test2(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print('test1 run time is %s'%(end_time-start_time))

test1 = test2(test1)