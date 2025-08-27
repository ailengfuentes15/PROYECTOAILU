
import pytest
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage


@pytest.fixture(scope="function")
def login_fixture():
   driver = BasePage.initialize_ChromeDriver()
   yield
   BasePage(driver).close_browser()