from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_validation():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/forgot_password")

    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "form_submit").click()

    assert "Internal Server Error" not in driver.page_source
    driver.save_screenshot("screenshots/form_validation.png")
    driver.quit()
