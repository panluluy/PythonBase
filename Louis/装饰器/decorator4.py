__author__ = "Louis-Pan"

username,password = 'pan','pan123'

def authentication(func):
    def wrapper(*args,**kwargs):
        username = input("pls enter your username：").strip()
        password = input('pls enter your password：').strip()
        if username=='pan' and password=='pan123':
            print('\033[32;1m %s 登录成功\033[0m'%username)
            return func(*args,**kwargs)
        else:
            exit('\033[31;1m 用户名或密码错误\033[0m')
    return wrapper


def index(): # 软件的首页
    print("welcome to index page")

@authentication  # home=authentication(home)
def home(): # 用户的首页，需要登录认证
    print("welcome to home page")
    return "from home"

@authentication
def bbs(): # 论坛页面，需要登录认证
    print("welcome to bbs page")

# 在home函数后return一个返回值，但是打印home函数的返回值，是None对象
# 因为func()函数是执行home函数，但是func()函数没有返回值，增加一个返回值即可
print(home())