__author__ = 'Louis-Pan'

import pytest

"""
传递的参数是单个的
"""

usernames = ['jerry','louis']

@pytest.fixture(params=usernames)
def login(request):
    print("数据准备")
    return request.param

# pytest中参数化的数据驱动，indirect=True表示把login当做函数去执行
@pytest.mark.parametrize("login",usernames,indirect=True)
def test_login(login):
    user = login
    print("测试用例中登录的用户名为：%s"%user)
    assert user in usernames

if __name__=="__main__":
    pytest.main(['-s','test_9_fixture_highest_parameterize.py'])