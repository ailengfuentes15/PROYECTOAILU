import pytest
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage


class TestLoginPage:

    def test_login_with_valid_credentials(self, login_fixture):
        login_fixture.navigate_to(login_fixture.url)
        login_fixture.enter_username()
        login_fixture.enter_password()
        login_fixture.click_login_button()
        assert "dashboard" in login_fixture.driver.current_url

    #def test_login_exitoso(self,driver):
        #login_page = LoginPage(self.driver)
        #login_page.navigate_to_login_page()
        #login_page.enter_username()
        #login_page.enter_password()
        #login_page.click_login_button()





