__author__ = 'Louis-Pan'

import pytest
"""
每个测试用例中都需要调用login，这样写很麻烦，可以使用autouse=True
"""
@pytest.fixture(scope="module",autouse=True)
def open_browser():
    print("\n打开浏览器，进入首页，登录成功")
    yield
    print("执行teardown")
    print("关闭浏览器")

def test_update_person_info():
    print("修改的测试用例")

def test_search():
    print("查询的测试用例")

def test_add_to_car():
    print("加入购物车的测试用例")

if __name__=="__main__":
    pytest.main(["-s",'test_5_fixture_scope_module_refactor.py'])