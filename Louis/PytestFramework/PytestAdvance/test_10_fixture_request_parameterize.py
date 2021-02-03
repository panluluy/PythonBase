__author__ = 'Louis-Pan'

import pytest
"""
传递的参数是多个的
"""

usernames = [{'username':'jerry',"password":123456},
             {"username":'louis',"password":654321}]

@pytest.fixture(params=usernames)
def login(request):
    print("数据准备")
    user = request.param['username']
    password = request.param["password"]

    if user=="jerry" and password==123456:
        return "登录成功"
    else:
        return "登录失败"

# pytest中参数化的数据驱动，indirect=True表示把login当做函数去执行
@pytest.mark.parametrize("login",usernames,indirect=True)
def test_login(login):
    user = login
    print("测试用例中登录的用户名为：%s"%user)
    assert user in "登录成功"

if __name__=="__main__":
    pytest.main(['-s','test_10_fixture_request_parameterize.py'])