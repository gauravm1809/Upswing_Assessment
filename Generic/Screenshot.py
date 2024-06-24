from datetime import datetime


def take_screenshot(driver):
    d = datetime.now().strftime("%d-%m-%y %H-%M-%S")
    driver.save_screenshot(f"../Screenshots/Screenshot{d}.png")
