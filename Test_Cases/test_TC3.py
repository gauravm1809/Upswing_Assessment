from Generic.verify_Title import *

from POM.HomePage import *


def test_TC3_1(setup):
    driver = setup
    verify_title(driver, "STORE")
    product_display_verification = HomePage(driver)
    product_display_verification.product_displayed_verification()


def test_TC3_2(setup):
    driver = setup
    verify_title(driver, "STORE")
    product_display_verification = HomePage(driver)
    product_display_verification.navigating_to_phones_category()


def test_TC3_3(setup):
    driver = setup
    verify_title(driver, "STORE")
    product_display_verification = HomePage(driver)
    product_display_verification.navigating_to_laptops_category()


def test_TC3_4(setup):
    driver = setup
    verify_title(driver, "STORE")
    product_display_verification = HomePage(driver)
    product_display_verification.navigating_to_monitors_category()
