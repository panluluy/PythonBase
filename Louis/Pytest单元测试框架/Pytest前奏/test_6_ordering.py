__author__ = 'Louis-Pan'

import pytest

value = 0

@pytest.mark.run(order=2)
def test_case1():
    print('我是测试用例1')
    assert value == 10


@pytest.mark.run(order=1)
def test_case2():
    print("我是测试用例2")
    global value
    value = 10
    assert value == 10

"""
pip install pytest-ordering安装执行顺序模块
执行 py.test test_6_ordering
"""