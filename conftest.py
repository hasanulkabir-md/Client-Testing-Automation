import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser(request):
    options = Options()
    options.add_argument("--headless")   # Run without opening Chrome window
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 800)
    yield driver
    # Save screenshot after each test
    os.makedirs("screenshots", exist_ok=True)
    fname = f"screenshots/{request.node.name}.png"
    driver.save_screenshot(fname)
    driver.quit()
