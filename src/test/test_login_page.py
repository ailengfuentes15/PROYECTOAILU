import pytest
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By
import time

@pytest.mark.regresion

class TestLogin:

    def test_login_exitoso(self):

        driver = BasePage.initialize_ChromeDriver()
        login_page = LoginPage(driver)
        login_page.open_url()
        login_page.enter_username()
        login_page.enter_password()
        login_page.click_login_button()

        texto_inicial = login_page.get_text(login_page.product_selector)

        assert "Products" in texto_inicial
        time.sleep (3)
        driver.quit()

    def test_login_fallido(self):

        driver = BasePage.initialize_ChromeDriver()
        login_page = LoginPage(driver)
        login_page.open_url()
        login_page.enter_userlocked()
        login_page.enter_password()
        time.sleep (2)
        login_page.click_login_button()

        texto_error = login_page.get_text((By.XPATH, "//h3[@data-test='error']"))


        assert "Epic sadface: Sorry, this user has been locked out." == texto_error
        time.sleep (3)
        driver.quit()

