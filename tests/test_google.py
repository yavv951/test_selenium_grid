import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_google_title(browser):
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    else:
        raise Exception("Browser not supported")

    #options.add_argument("--headless")  # Можно убрать, если используешь VNC
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )
    driver.get("https://www.google.com")
    time.sleep(20)
    assert "Google" in driver.title
    driver.quit()