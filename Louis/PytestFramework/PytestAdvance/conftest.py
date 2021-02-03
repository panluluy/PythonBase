__author__ = 'Louis-Pan'

import pytest

"""
此文件是一个公共的函数，并且文件名必须是conftest.py
"""

@pytest.fixture()
def login():
    print("\n登录成功")