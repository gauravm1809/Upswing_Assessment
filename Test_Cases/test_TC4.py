from Generic.verify_Title import *

from POM.HomePage import *


def test_TC4_1(setup):
    driver = setup
    verify_title(driver, "STORE")
    adding_product = HomePage(driver)
    adding_product.adding_products_to_the_cart()
    