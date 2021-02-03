__author__ = 'Louis-Pan'

import pytest


def setup_module():
    print('整个模块.py开始')


def teardown_module():
    print('整个模块.py结束')


def setup_function():
    print('不在类中的函数前')


def teardown_function():
    print('不在类中的函数后')


def test_w_one():
    print('不在类中的方法1')


def test_w_two():
    print('不在类中的方法2')


class TestClass:
    def setup_class(self):
        print('类前面')

    def teardown_class(self):
        print('类之后')

    def setup_method(self):
        print('方法前')

    def teardown_method(self):
        print('方法后')

    def test_one(self):
        x = "this"
        assert "h5" in x

    def test_two(self):
        x = "hello"
        assert "hello1" == x

    def test_three(self):
        a = "hello1"
        b = "hello world"
        assert a in b


if __name__ == '__main__':
    # pytest.main(["-k","TestClass and test_three"])
    """
    -k：根据条件执行
    pytest -k "TestClass and test_three"
    只能在命令行中执行，遍历所有脚本，只执行TestClass类下test_three用例
    
    pytest -k "TestClass and test_three" test_14_run_condition_case.py
    指定脚本中运行TestClass类下test_three用例
    
    pytest -k "TestClass or test_w_two" test_14_run_condition_case.py
    在test_14_run_condition_case.py脚本中
    执行TestClass类中所有的用例，或者test_w_two不在类中的方法
    
    -x：运行失败达到几次停止
    pytest -v -s -x test_14_run_condition_case.py --maxfail=2
    执行test_14_run_condition_case.py脚本时，如果出现了2次错误，停止脚本执行
    """
