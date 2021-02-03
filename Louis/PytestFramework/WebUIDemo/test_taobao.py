__author__ = 'Louis-Pan'

import pytest
import time


def test_taobao(driver):
    driver.get("https://www.taobao.com/")
    driver.maximize_window()
    driver.find_element_by_id("ks-component161").send_keys("iphone")
    time.sleep(1)
    title = driver.title
    print("测试结果：%s" % title)
    assert '淘宝' in title


if __name__ == '__main__':
    pytest.main(['-s', 'test_taobao.py'])