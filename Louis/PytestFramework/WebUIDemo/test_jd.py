__author__ = 'Louis-Pan'

import pytest
import time


def test_jd(driver):
    driver.get("https://www.jd.com/")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_id("key").send_keys("iphone12")
    title = driver.title
    print("测试结果：%s" % title)
    assert '京东' in title


if __name__ == '__main__':
    pytest.main(['-s', 'test_jd.py'])