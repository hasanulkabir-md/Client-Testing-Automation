import os
from selenium.webdriver.common.by import By

def test_file_upload(browser, tmp_path):
    test_file = tmp_path / "hello.txt"
    test_file.write_text("Hello Recruiter!")

    browser.get("https://the-internet.herokuapp.com/upload")
    upload_input = browser.find_element(By.ID, "file-upload")
    upload_input.send_keys(str(test_file))
    browser.find_element(By.ID, "file-submit").click()

    uploaded = browser.find_element(By.ID, "uploaded-files").text
    assert "hello.txt" in uploaded
