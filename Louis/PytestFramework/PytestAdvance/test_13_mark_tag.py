__author__ = 'Louis-Pan'

import pytest

# webui为标签名
@pytest.mark.webui
def test_webui():
    pass

@pytest.mark.ios
def test_ios():
    pass

@pytest.mark.android
def test_android():
    pass

if __name__ == '__main__':
    pytest.main(['-s','test_13_mark_tag.py'])

"""
此种用法只能在终端中使用

运行标签中不是ios的用例
pytest -s -v test_13_mark_tag.py -m "not ios"

运行标签中是webui的用例
pytest -s -v test_13_mark_tag.py -m webui

"""