__author__ = 'Louis-Pan'

import pytest

"""
pytest.assume()方法可以进行多次断言
pip install pytest-assume安装
"""
def test_func():
    pytest.assume(1==1)
    pytest.assume(1==2)
    pytest.assume(3==3)