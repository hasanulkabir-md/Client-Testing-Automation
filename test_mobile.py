from time import sleep
from appium import webdriver
from appium.options.android import UiAutomator2Options

def test_launch_settings():
    # If 'adb devices' shows a different ID, update deviceName below
    opts = UiAutomator2Options()
    opts.set_capability("platformName", "Android")
    opts.set_capability("appium:automationName", "UiAutomator2")
    opts.set_capability("appium:deviceName", "emulator-5554")
    opts.set_capability("appium:noReset", True)

    # Launch the built-in Settings app (no APK download needed)
    opts.set_capability("appium:appPackage", "com.android.settings")
    opts.set_capability("appium:appActivity", "com.android.settings.Settings")

    # Appium v3 uses root base path (no /wd/hub)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=opts)

    sleep(2)
    # Verify Settings is in foreground
    assert driver.current_package == "com.android.settings"

    # Optional proof
    driver.save_screenshot("screenshots/settings_open.png")
    driver.quit()
