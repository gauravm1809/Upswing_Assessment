from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from time import sleep


class AddToCart:

    def __init__(self, driver):
        self.driver = driver

    def checkout_by_adding_product_in_cart(self):
        self.driver.find_element("xpath", "//a[.='Samsung galaxy s6']").click()
        self.driver.find_element("xpath", "//a[@onclick='addToCart(1)']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present())
        a = self.driver.switch_to.alert
        assert a.text == "Product added"
        print("Product successfully added to cart.")
        ok = self.driver.switch_to.alert
        ok.accept()
        self.driver.find_element("xpath", "//a[.='Cart']").click()
        sleep(2)
        product_in_cart = self.driver.find_element("xpath", "//tr[@class='success']//td[2]")
        if product_in_cart.text == "Samsung galaxy s6":
            print("Product added in the cart and checked successfully.")

    def checkout_without_adding_product_in_cart(self):
        self.driver.find_element("xpath", "//a[.='Cart']").click()
        self.driver.find_element("xpath", "//button[@data-target='#orderModal']").click()
        self.driver.find_element("xpath", "//input[@id='name']").send_keys("gm")
        self.driver.find_element("xpath", "//input[@id='country']").send_keys("india")
        self.driver.find_element("xpath", "//input[@id='city']").send_keys("blr")
        self.driver.find_element("xpath", "//input[@id='card']").send_keys("123456789012")
        self.driver.find_element("xpath", "//input[@id='month']").send_keys("june")
        self.driver.find_element("xpath", "//input[@id='year']").send_keys("2024")
        self.driver.find_element("xpath", "//button[.='Purchase']").click()
        confirmation = self.driver.find_element("xpath", "//h2[.='Thank you for your purchase!']")
        assert confirmation.text == "Thank you for your purchase!"
