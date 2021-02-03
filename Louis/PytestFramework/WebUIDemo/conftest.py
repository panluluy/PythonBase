__author__ = 'Louis-Pan'

import pytest
from selenium import webdriver

# scope="session"表示全局的，可以跨文件调用driver
@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Chrome(
        executable_path=r'F:\PythonBase\Louis\PytestFramework\WebUIDemo\driver\chromedriver.exe')

    def close_browser():
        driver.quit()

    request.addfinalizer(close_browser)
    return driver