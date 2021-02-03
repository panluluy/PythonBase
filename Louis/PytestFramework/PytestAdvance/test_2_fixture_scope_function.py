__author__ = 'Louis-Pan'

import pytest

"""
使用场景：有的用例需要登录执行，有些用例不需要登录执行
用例在执行时需要登录的用例，都需要执行login函数，相当于unittest中setUp()函数，每条用例运行前都需要执行

步骤：
1. 导⼊pytest
2. 在登陆的函数上⾯加@pytest.fixture()
3. 在要使⽤的测试⽅法中传⼊（登陆函数名称），就先登陆
4. 不传⼊的就不登陆直接执⾏测试⽅法。
"""
@pytest.fixture(scope="function")
def login():
    print("\n登录成功")

def test_update_person_info(login):
    print("登录成功后修改个人信息")

def test_search():
    print("无需登录，查询商品")

def test_add_to_car(login):
    print("登录成功后加入商品至购物车")

if __name__=="__main__":
    pytest.main(["-s",'test_2_fixture_scope_function.py'])
