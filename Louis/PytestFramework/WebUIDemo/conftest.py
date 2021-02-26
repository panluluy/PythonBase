__author__ = 'Louis-Pan'

import pytest
from selenium import webdriver
import allure

@allure.feature("打开浏览器")
@pytest.fixture(scope="function")
def driver():
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    option.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])
    browser = webdriver.Chrome(chrome_options=option,
        executable_path=r'E:\Github\PythonBase\Louis\PytestFramework\WebUIDemo\driver\chromedriver.exe')
    return browser