__author__ = 'Louis-Pan'

import pytest
"""
你已经可以将测试⽅法前要执⾏的或依赖的解决了，测试⽅
法后销毁清除数据的要如何进⾏呢？范围是模块级别的。类似setupClass

解决：通过在同⼀模块中加⼊ yield关键字，yield是调⽤第⼀次返
回结果，第⼆次执⾏它下⾯的语句返回。

用例在执行时只需要打开一次浏览器，将所有的用例执行完后，再执行teardown动作，相当于unittest中setUpClass()函数

"""
@pytest.fixture(scope="module")
def login():
    print("\n打开浏览器，进入首页，登录成功")
    yield
    print("执行teardown")
    print("关闭浏览器")

def test_update_person_info(login):
    print("登录成功后修改个人信息")

def test_search():
    print("无需登录，查询商品")

def test_add_to_car(login):
    print("需要登录，加入商品至购物车")

if __name__=="__main__":
    pytest.main(["-s",'test_4_fixture_scope_module.py'])