from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from Generic.Screenshot import *


def verify_title(driver, etitle):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.title_is(etitle))
    except:
        take_screenshot(driver)
        raise Exception("Title Not Matches")
