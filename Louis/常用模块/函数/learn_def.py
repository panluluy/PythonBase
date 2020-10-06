__author__="Louis-Pan"

with open('log.txt','a+') as f:
    f.write("end of action \n")

def test1():
    print("I am test1")
    with open('log.txt', 'a+') as f:
        f.write("end of action \n")

def test2():
    print("I am test2")
    with open('log.txt', 'a+') as f:
        f.write("end of action \n")

def test3():
    print("I am test3")
    with open('log.txt', 'a+') as f:
        f.write("end of action \n")

test1()
test2()
test3()