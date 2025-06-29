import pytest
import allure

@allure.title("Проверка заголовка Google")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_google_title(driver):
    with allure.step("Открываем Google"):
        driver.get("https://www.google.com")

    with allure.step("Проверяем заголовок"):
        assert "Google" in driver.title