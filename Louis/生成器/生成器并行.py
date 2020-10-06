__author__ = 'Louis-Pan'
import time

def consumer(name):
    print("%s 开始吃包子啦！" %name)
    while True:
        baozi = yield
        print("包子%s来了，被%s吃了一半！"%(baozi,name))

# c = consumer('louis')
# # c.__next__()
# # baozi = '猪肉馅'
# # c.send(baozi)

def productor(name):
    c1 = consumer("A")
    c2 = consumer("B")
    c1.__next__()
    c2.__next__()
    print("%s 开始做包子啦！"% name)
    for i in range(1,10):
        time.sleep(1)
        print("做了一个包子，分成两半")
        c1.send(i)
        c2.send(i)

productor('louis')