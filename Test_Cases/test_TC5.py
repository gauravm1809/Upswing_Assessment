from Generic.verify_Title import *

from POM.Add_to_Cart import *


def test_TC4_1(setup):
    driver = setup
    verify_title(driver, "STORE")
    checkout_of_product = AddToCart(driver)
    checkout_of_product.checkout_by_adding_product_in_cart()


def test_TC4_2(setup):
    driver = setup
    verify_title(driver, "STORE")
    checkout_of_product = AddToCart(driver)
    checkout_of_product.checkout_without_adding_product_in_cart()

