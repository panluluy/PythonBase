__author__="Louis-Pan"
"""
代码的重用；函数的一致性；可扩展
"""
import time
def logger():
    current_time = time.strftime("%Y-%m-%d %X")
    with open('log.txt','a+') as f:
        f.write("%s end of action \n"%current_time)

def test1():
    print("I am test1")
    logger()

def test2():
    print("I am test2")
    logger()

def test3():
    print("I am test3")
    logger()
