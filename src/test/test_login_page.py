import pytest
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage


class TestLoginPage:

    @pytest.fixture
    def driver(self, driver):
        # setup → antes del test
        driver = BasePage.initialize_ChromeDriver_headless()
        driver.max_window()
        yield driver
        # teardown → despues del test
        driver.quit()

    def test_login_exitoso(self,driver):
        login_page = LoginPage(self.driver)
        login_page.navigate_to_login_page()
        login_page.enter_username()
        login_page.enter_password()
        login_page.click_login_button()





