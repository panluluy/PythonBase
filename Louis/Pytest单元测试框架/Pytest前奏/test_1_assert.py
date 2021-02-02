__author__ = 'Louis-Pan'

"""
pytest命名规范：
1.文件名必须以test开头
2.类名必须以Test开头，并且不能有__init__方法
3.函数名即用例名必须以test开头

命令行中执行有高亮显示需要安装pip install pytest-sugar
执行时通过：py.test test_1.assert.py
"""

def func(a,b):
    return a + b

def test_func():
    assert func(1,2) == 3


