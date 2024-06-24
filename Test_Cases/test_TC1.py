from Generic.verify_Title import *

from POM.HomePage import *


def test_TC1_1(setup):
    driver = setup
    verify_title(driver, "STORE")
    _signup = HomePage(driver)
    _signup.sign_up_button()
    _signup.username()
    _signup.password("12345")
    _signup.click_on_register_button()
    _signup.alert_confirmation_popup_for_successful_account_registration()


def test_TC1_2(setup):
    driver = setup
    verify_title(driver, "STORE")
    _signup = HomePage(driver)
    _signup.sign_up_button()
    _signup.blank_username("")
    _signup.blank_password("")
    _signup.click_on_register_button_for_blank_fields()
    _signup.alert_confirmation_popup_for_failed_account_registration()
