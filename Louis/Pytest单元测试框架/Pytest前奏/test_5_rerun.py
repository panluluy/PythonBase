__author__ = 'Louis-Pan'

import random

def func(x,y):
    return x + y

def test_func():
    result = random.randint(1,5)
    print(result)
    assert func(1,2) == result

"""
pip install pytest-rerunfailures 安装失败重跑模块

执行的命令：py.test --reruns 5 test_5_rerun.py
"""