__author__ = 'Louis-Pan'

import pytest
import time


def test_51job(driver):
    driver.get("https://www.51job.com/")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_id("kwdselectid").send_keys("软件测试工程师")
    title = driver.title
    print("测试结果：%s" % title)
    assert '招聘' in title


if __name__ == '__main__':
    pytest.main(['-s', 'test_51job.py'])