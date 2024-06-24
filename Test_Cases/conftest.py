import pytest

from selenium.webdriver import Chrome


@pytest.fixture
def setup():
    driver = Chrome()
    driver.implicitly_wait(20)
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
