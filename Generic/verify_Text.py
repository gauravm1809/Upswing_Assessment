from Generic.Screenshot import *


def verify_text(atext, etext, driver):
    try:
        assert atext == etext
    except:
        take_screenshot(driver)
        raise Exception

