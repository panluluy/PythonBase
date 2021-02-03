__author__ = 'Louis-Pan'

import pytest
import time


def test_baidu(driver):
    driver.get('https://www.baidu.com')
    driver.maximize_window()
    driver.find_element_by_id("kw").send_keys("自动化测试")
    driver.find_element_by_id("su").click()
    time.sleep(1)
    title = driver.title
    print("测试结果：%s" % title)
    assert '自动化测试' in title


if __name__ == '__main__':
    pytest.main(['-v', 'test_baidu.py'])