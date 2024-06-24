from datetime import datetime

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from time import sleep

from xlrd import *

from Generic.verify_Text import *


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def sign_up_button(self):
        self.driver.find_element("xpath", "//a[@id='signin2']").click()

    def username(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%S")
        self.driver.find_element("xpath", "//input[@id='sign-username']").send_keys("gm" + time_stamp + "@gmail.com")

    def blank_username(self, data):
        self.driver.find_element("xpath", "//input[@id='sign-username']").send_keys(data)

    def password(self, data):
        self.driver.find_element("xpath", "//input[@id='sign-password']").send_keys(data)

    def blank_password(self, data):
        self.driver.find_element("xpath", "//input[@id='sign-password']").send_keys(data)

    def click_on_register_button(self):
        self.driver.find_element("xpath", "//button[@onclick='register()']").click()

    def click_on_register_button_for_blank_fields(self):
        self.driver.find_element("xpath", "//button[@onclick='register()']").click()

    def alert_confirmation_popup_for_successful_account_registration(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        a = self.driver.switch_to.alert
        assert a.text == "Sign up successful.", "Sign up is not successful."

    def alert_confirmation_popup_for_failed_account_registration(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        a = self.driver.switch_to.alert
        assert a.text == "Please fill out Username and Password."

    def login_button(self):
        self.driver.find_element("xpath", "//a[.='Log in']").click()

    def username_and_password_for_login(self):
        wb = open_workbook("../Excel/Data_userDetails.xlsx")
        sh = wb.sheet_by_name("User_data")
        row_count = sh.nrows
        _l = [sh.row_values(i) for i in range(1, row_count)]
        for un, pwd in _l:
            self.driver.find_element("xpath", "//input[@id='loginusername']").send_keys(un)
            sleep(2)
            self.driver.find_element("xpath", "//input[@id='loginpassword']").send_keys(pwd)
            return _l

    def valid_username_and_password_for_login_for_data_2(self):
        wb = open_workbook("../Excel/Data_userDetails.xlsx")
        sh = wb.sheet_by_name("User_data")
        row_count = sh.nrows
        _l = [sh.row_values(i) for i in range(2, row_count)]
        for un, pwd in _l:
            self.driver.find_element("xpath", "//input[@id='loginusername']").send_keys(un)
            sleep(2)
            self.driver.find_element("xpath", "//input[@id='loginpassword']").send_keys(pwd)
            return _l

    def valid_username_and_password_for_login_for_data_3(self):
        wb = open_workbook("../Excel/Data_userDetails.xlsx")
        sh = wb.sheet_by_name("User_data")
        row_count = sh.nrows
        _l = [sh.row_values(i) for i in range(3, row_count)]
        for un, pwd in _l:
            self.driver.find_element("xpath", "//input[@id='loginusername']").send_keys(un)
            sleep(2)
            self.driver.find_element("xpath", "//input[@id='loginpassword']").send_keys(pwd)
            return _l

    def invalid_username_and_password_for_login_for_data_1(self):
        wb = open_workbook("../Excel/Data_userDetails.xlsx")
        sh = wb.sheet_by_name("Invalid_userData")
        row_count = sh.nrows
        _l = [sh.row_values(i) for i in range(1, row_count)]
        for un, pwd in _l:
            self.driver.find_element("xpath", "//input[@id='loginusername']").send_keys(un)
            sleep(2)
            self.driver.find_element("xpath", "//input[@id='loginpassword']").send_keys(pwd)
            return _l

    def invalid_username_and_password_for_login_for_data_2(self):
        wb = open_workbook("../Excel/Data_userDetails.xlsx")
        sh = wb.sheet_by_name("Invalid_userData")
        row_count = sh.nrows
        _l = [sh.row_values(i) for i in range(2, row_count)]
        for un, pwd in _l:
            self.driver.find_element("xpath", "//input[@id='loginusername']").send_keys(un)
            sleep(2)
            self.driver.find_element("xpath", "//input[@id='loginpassword']").send_keys(pwd)
            return _l

    def invalid_username_and_password_for_login_for_data_3(self):
        wb = open_workbook("../Excel/Data_userDetails.xlsx")
        sh = wb.sheet_by_name("Invalid_userData")
        row_count = sh.nrows
        _l = [sh.row_values(i) for i in range(3, row_count)]
        for un, pwd in _l:
            self.driver.find_element("xpath", "//input[@id='loginusername']").send_keys(un)
            sleep(2)
            self.driver.find_element("xpath", "//input[@id='loginpassword']").send_keys(pwd)
            return _l

    def click_on_login_button(self):
        self.driver.find_element("xpath", "//button[@onclick='logIn()']").click()

    def alert_confirmation_popup_for_successful_login(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element(("xpath", "//a[contains(.,'Welcome')]"), "Welcome"))

    def alert_confirmation_for_invalid_credentials_for_login(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        a = self.driver.switch_to.alert
        assert a.text == "User does not exist." or a.text == "Wrong password."

    def click_on_logout_button(self):
        self.driver.find_element("xpath", "//a[.='Log out']").click()

    def product_displayed_verification(self):
        _products = self.driver.find_elements("xpath", "//div[@class='col-lg-9']//h4//a")
        for product_name in _products:
            if product_name.is_displayed():
                print(product_name.text)

    def navigating_to_phones_category(self):
        self.driver.find_element("xpath", "//a[.='Phones']").click()
        sleep(2)
        phones_category = self.driver.find_elements("xpath", "//div[@class='col-lg-4 col-md-6 mb-4']//h4")
        for names_of_phones in phones_category:
            if (names_of_phones.text == "HTC One M9" and "Samsung galaxy s6" and "Nokia lumia 1520" and "Nexus 6"
                    and "Samsung galaxy s7" and "Iphone 6 32gb" and "Sony xperia z5"):
                print("Successfully navigated to the phones category.")

    def navigating_to_laptops_category(self):
        self.driver.find_element("xpath", "//a[.='Laptops']").click()
        sleep(2)
        laptops_category = self.driver.find_elements("xpath", "//div[@class='col-lg-4 col-md-6 mb-4']//h4")
        for names_of_laptops in laptops_category:
            if (names_of_laptops.text == "Sony vaio i5" and "Sony vaio i7" and "MacBook air" and "Dell i7 8gb"
                    and "2017 Dell 15.6 Inch" and "MacBook Pro"):
                print("Successfully navigated to the Laptops category.")

    def navigating_to_monitors_category(self):
        self.driver.find_element("xpath", "//a[.='Monitors']").click()
        sleep(2)
        monitors_category = self.driver.find_elements("xpath", "//div[@class='col-lg-4 col-md-6 mb-4']//h4")
        for names_of_monitors in monitors_category:
            if names_of_monitors.text == "Apple monitor 24" and "ASUS VS247H-P 23.6- Inch Full HD ":
                print("Successfully navigated to the Monitors category.")

    def adding_products_to_the_cart(self):
        self.driver.execute_script(f"window.scrollTo(0, 3000)")
        sleep(3)
        self.driver.find_element("xpath", "//button[@id='next2']").click()
        self.driver.find_element("xpath", "//a[.='MacBook Pro']").click()
        self.driver.find_element("xpath", "//a[@onclick='addToCart(15)']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        a = self.driver.switch_to.alert
        assert a.text == "Product added"

    def check_logout_is_successful(self):
        self.driver.find_element("xpath", "//a[.='Log in']").click()
        self.driver.find_element("xpath", "//input[@id='loginusername']").send_keys("gm20@gmail.com")
        sleep(2)
        self.driver.find_element("xpath", "//input[@id='loginpassword']").send_keys("12345a")
        self.driver.find_element("xpath", "//button[@onclick='logIn()']").click()
        sleep(2)
        self.driver.find_element("xpath", "//a[@onclick='logOut()']").click()
        if self.driver.find_element("xpath", "//a[@id='login2']").is_displayed():
            print("Logout Successful.")
