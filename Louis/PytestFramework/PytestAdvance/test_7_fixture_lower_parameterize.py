__author__ = 'Louis-Pan'

import pytest

@pytest.fixture(params=['jerry','louis'])
def login(request):  # 此处的形参必须是request，已经写死了
    user = request.param
    print("\n打开首页，登录的用户为：%s"%user)
    return user

def test_login(login):
    print(login)

if __name__=="__main__":
    pytest.main(['-s','test_7_fixture_lower_parameterize.py'])