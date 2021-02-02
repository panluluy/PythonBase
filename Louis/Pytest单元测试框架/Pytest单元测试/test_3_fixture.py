__author__ = 'Louis-Pan'

import pytest

"""
你与其他测试⼯程师合作⼀起开发时，公共的模块要在不同⽂
件中，要在⼤家都访问到的地⽅。
解决：使⽤conftest.py 这个⽂件进⾏数据共享，并且他可以放在不同位置起着不同的范围共享作⽤。

login写到公共的conftest.py文件中，并且不需要导入即可使用
"""

def test_update_person_info(login):
    print("登录成功后修改个人信息")

def test_search():
    print("无需登录，查询商品")

def test_add_to_car(login):
    print("需要登录，加入商品至购物车")

# 不在类中的函数前，必须这样写，否则不会执行
def setup_function():
    print("**********")

# 不在类中的函数后，必须这样写，否则不会执行
def teardown_function():
    print("===============")

if __name__=="__main__":
    pytest.main(["-s",'test_3_fixture.py'])
