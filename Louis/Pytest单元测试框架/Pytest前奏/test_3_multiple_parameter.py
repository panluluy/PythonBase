__author__ = 'Louis-Pan'

import pytest

@pytest.mark.parametrize("x,y",[
    (1+2,3),
    (3+5,6),
    ("tashi","tashi"),
    ])

# 注意test_add函数中形参必须与@pytest.mark.parametrize中x,y命名一致，否则报错
def test_add(x,y):
    assert x == y