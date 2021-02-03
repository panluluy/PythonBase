__author__ = 'Louis-Pan'

import pytest

usernames = ["Jerry","","tashi"]
passwords = ["123456",'',"tashi123"]

# 增加scope是全局的，只执行一次，否则，每执行一条用例都会执行一遍数据准备
@pytest.fixture(scope="module",params=usernames)
def user_name(request):
    print("数据准备")
    username = request.param
    return username

@pytest.fixture(scope="module",params=passwords)
def pass_word(request):
    print("数据准备")
    password = request.param
    return password

# pytest中参数化的数据驱动，indirect=True表示把login当做函数去执行
# 从下往上执行
# 两个数据进行组合测试有3*3个测试用例执行
@pytest.mark.parametrize("pass_word",passwords,indirect=True)
@pytest.mark.parametrize("user_name",usernames,indirect=True)
def test_login(user_name,pass_word):
    username = user_name
    password = pass_word
    print("测试用例中登录的用户名为：%s，密码为：%s"%(username,password))
    assert username=="Jerry" and password=="123456"

if __name__=="__main__":
    pytest.main(['-s','test_11_fixture_request_parameterize_1.py'])