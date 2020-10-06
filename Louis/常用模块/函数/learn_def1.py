__author__="Louis-Pan"
"""
代码的重用；函数的一致性
"""
def logger()
    with open('log.txt','a+') as f:
        f.write("end of action \n")

def test1():
    print("I am test1")
    logger()

def test2():
    print("I am test2")
    logger()

def test3():
    print("I am test3")
    logger()

test1()
test2()
test3()