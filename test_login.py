import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_flow(browser):
    browser.get("https://the-internet.herokuapp.com/login")

    # Invalid login
    browser.find_element(By.ID, "username").send_keys("wrong")
    browser.find_element(By.ID, "password").send_keys("wrong", Keys.RETURN)
    error = browser.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in error

    # Valid login
    browser.find_element(By.ID, "username").clear()
    browser.find_element(By.ID, "password").clear()
    browser.find_element(By.ID, "username").send_keys("tomsmith")
    browser.find_element(By.ID, "password").send_keys("SuperSecretPassword!", Keys.RETURN)
    success = browser.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success

    # ✅ Save screenshot after successful login
    os.makedirs("screenshots", exist_ok=True)
    # browser.save_screenshot("screenshots/test_login.png")
