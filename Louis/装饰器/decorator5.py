__author__ = "Louis-Pan"

username,password = 'pan','pan123'

def authentication(auth_type):
    print('authentication func :',auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            print("wrapper is :",*args,**kwargs)
            if auth_type=='local':
                username = input("pls enter your username：").strip()
                password = input('pls enter your password：').strip()
                if username==username and password== password:
                    print('\033[32;1m %s 登录成功\033[0m'%username)
                    return func(*args,**kwargs)
                else:
                    exit('\033[31;1m 用户名或密码错误\033[0m')
            elif auth_type=='ldap':
                print('从ldap中获取用户名密码校验')
        return wrapper
    return outer_wrapper

def index(): # 软件的首页
    print("welcome to index page")

@authentication(auth_type='local')  # home=authentication(home)
def home(): # 用户的首页，需要登录认证
    print("welcome to home page")
    return "from home"

@authentication(auth_type='ldap')
def bbs(): # 论坛页面，需要登录认证
    print("welcome to bbs page")

# 在home函数后return一个返回值，但是打印home函数的返回值，是None对象
# 因为func()函数是执行home函数，但是func()函数没有返回值，增加一个返回值即可
index()
print(home())
bbs()