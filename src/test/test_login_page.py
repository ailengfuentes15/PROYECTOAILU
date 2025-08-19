import pytest
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage


class TestLoginPage:
    @pytest.fixture(scope="class")
    def setup(self):
        """Inicializa el WebDriver y la página de login."""
        self.driver = BasePage.initialize_ChromeDriver_headless()
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.quit()

    def test_login(self, setup):
        """Prueba el proceso de inicio de sesión."""
        self.login_page.navigate_to_login_page("https://www.saucedemo.com/")
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login_button()

        # Aquí podrías agregar aserciones para verificar que el inicio de sesión fue exitoso.
        ####mañanaborrar esto esta mal####