from Generic.verify_Title import *

from POM.HomePage import *


def test_TC6_1(setup):
    driver = setup
    verify_title(driver, "STORE")
    logout = HomePage(driver)
    logout.check_logout_is_successful()
