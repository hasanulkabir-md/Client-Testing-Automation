from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation(browser):
    browser.get("https://the-internet.herokuapp.com/forgot_password")
    email_box = browser.find_element(By.ID, "email")
    email_box.send_keys("test@example.com")
    browser.find_element(By.ID, "form_submit").click()

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert "Internal Server Error" not in browser.page_source
