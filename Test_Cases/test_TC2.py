from Generic.verify_Title import *

from POM.HomePage import *


def test_TC2_1(setup):
    driver = setup
    verify_title(driver, "STORE")
    _login = HomePage(driver)
    _login.login_button()
    _login.username_and_password_for_login()
    _login.click_on_login_button()
    _login.alert_confirmation_popup_for_successful_login()
    _login.click_on_logout_button()


def test_TC_2(setup):
    driver = setup
    verify_title(driver, "STORE")
    _login = HomePage(driver)
    _login.login_button()
    _login.valid_username_and_password_for_login_for_data_2()
    _login.click_on_login_button()
    _login.alert_confirmation_popup_for_successful_login()
    _login.click_on_logout_button()


def test_TC_2_3(setup):
    driver = setup
    verify_title(driver, "STORE")
    _login = HomePage(driver)
    _login.login_button()
    _login.valid_username_and_password_for_login_for_data_3()
    _login.click_on_login_button()
    _login.alert_confirmation_popup_for_successful_login()
    _login.click_on_logout_button()


def test_TC2_4(setup):
    driver = setup
    verify_title(driver, "STORE")
    _login = HomePage(driver)
    _login.login_button()
    _login.invalid_username_and_password_for_login_for_data_1()
    _login.click_on_login_button()
    _login.alert_confirmation_for_invalid_credentials_for_login()


def test_TC2_5(setup):
    driver = setup
    verify_title(driver, "STORE")
    _login = HomePage(driver)
    _login.login_button()
    _login.invalid_username_and_password_for_login_for_data_2()
    _login.click_on_login_button()
    _login.alert_confirmation_for_invalid_credentials_for_login()


def test_TC2_6(setup):
    driver = setup
    verify_title(driver, "STORE")
    _login = HomePage(driver)
    _login.login_button()
    _login.invalid_username_and_password_for_login_for_data_3()
    _login.click_on_login_button()
    _login.alert_confirmation_for_invalid_credentials_for_login()

