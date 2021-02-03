__author__ = 'Louis-Pan'

import pytest
"""
不想原测试⽅法有任何改动，或全部都⾃动实现⾃动应⽤，没特
例，也都不需要返回值时可以选择⾃动应⽤
"""
@pytest.fixture()
def open_browser():
    print("\n打开浏览器，进入首页，登录成功")
    yield
    print("执行teardown")
    print("关闭浏览器")

@pytest.mark.usefixtures("open_browser")
def test_update_person_info():
    print("登录成功后，执行修改的测试用例")

def test_search():
    print("无需登录，执行查询的测试用例")

@pytest.mark.usefixtures("open_browser")
def test_add_to_car():
    print("登录成功后，执行加入购物车的测试用例")

if __name__=="__main__":
    pytest.main(["-s",'test_6_fixture_mark_usefixtures.py'])