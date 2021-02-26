__author__ = 'Louis-Pan'
import pytest
import allure
import time
from selenium import webdriver

class TestEcshop():

    @allure.feature('打开Ecshop')
    @pytest.fixture(scope='function',autouse=True)
    def start(self,driver):
        with allure.step('step one:打开浏览器输入Ecshop网址'):
            driver.get('http://www.tsecshop.com/user.php')
            driver.maximize_window()
            time.sleep(1)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.feature('Ecshop登录功能')
    @allure.story('正确的用户名，正确的密码')
    def test_login_success(self, driver):
        with allure.step('step two：输入正确的用户名和正确的密码'):
            driver.find_element_by_name("username").send_keys('tashi10')
            driver.find_element_by_name("password").send_keys("123456")
            driver.find_element_by_name("submit").click()
            result = driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/a[1]').text
            time.sleep(1)
            assert 'tashi10' in result
            driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature('Ecshop登录功能')
    @allure.story('错误的用户名，正确的密码')
    def test_login_username_wrong(self, driver):
        with allure.step('step two：输入错误的用户名和正确的密码'):
            driver.find_element_by_name("username").send_keys('tashi00')
            driver.find_element_by_name("password").send_keys("123456")
            driver.find_element_by_name("submit").click()
            result = driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/a[1]').text
            time.sleep(1)
            assert '登录' in result
            driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature('Ecshop登录功能')
    @allure.story('正确的用户名，错误的密码')
    def test_login_password_wrong(self, driver):
        with allure.step('step two：输入正确的用户名和错误的密码'):
            driver.find_element_by_name("username").send_keys('tashi10')
            driver.find_element_by_name("password").send_keys("123457")
            driver.find_element_by_name("submit").click()
            result = driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/a[1]').text
            time.sleep(1)
            assert '登录' in result
            driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature('Ecshop登录功能')
    @allure.story('用户名为空')
    def test_login_username_empty(self, driver):
        with allure.step('step two：用户名为空'):
            # driver.find_element_by_name("username").send_keys('tashi10')
            driver.find_element_by_name("password").send_keys("123457")
            driver.find_element_by_name("submit").click()
            result = driver.switch_to.alert.text
            time.sleep(1)
            assert '用户名不能为空' in result
            driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature('Ecshop登录功能')
    @allure.story('密码为空')
    def test_login_password_empty(self, driver):
        with allure.step('step two：密码为空'):
            driver.find_element_by_name("username").send_keys('tashi10')
            # driver.find_element_by_name("password").send_keys("123457")
            driver.find_element_by_name("submit").click()
            result = driver.switch_to.alert.text
            time.sleep(1)
            assert '登录密码不能为空' in result
            driver.quit()

if __name__ == '__main__':
    pytest.main()

    """
    Terminal中执行pytest -s -v test_ecshop.py --allure-severities blocker,normal
    如果在执行过程中提示warning，添加pytest.ini文件，在文件中添加忽略warning选项
    """