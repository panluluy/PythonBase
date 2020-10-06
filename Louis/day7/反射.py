__author__ = "Alex Li"

class Dog(object):

    def __init__(self,name):
        self.name = name

    def eating(self):
        print("%s is eating 。。。。。"%self.name)

def sing(self):
    print("%s is singing....."%self.name)


d = Dog("Tom")
# choice = input(">>>").strip()
# # 判断类的实例对象中是否有choice输入的属性
# print(hasattr(d,choice))

choice = input(">>>").strip()
if hasattr(d,choice):
    func = getattr(d,choice)
    func()
else:
    # setattr(d,choice,sing)  # 增加一个d.choice属性，调用外层函数sing
    # print(d.song(d))    # 需要将自身传递进去

    setattr(d,choice,22)
    print(getattr(d,choice))
    print(hasattr(d,choice))