import pytest
from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By
import time


class TestLogin:

    def test_login_exitoso(self):

        driver = BasePage.initialize_ChromeDriver()
        login_page = LoginPage(driver)
        login_page.open_url()
        login_page.enter_username()
        login_page.enter_password()

        texto_inicial = login_page.get_text(login_page.titulo_inicio)

        assert "Swag Labs" in texto_inicial
        time.sleep(3)
        login_page.click_login_button()

        driver.quit()

#def detest_login(self):
        # Abrir URL desde JSON

        #self.login_page_con_json.login_json()
        # Verificar que el login fue exitoso
        #products_text = self.login_page_con_json.get_text(self.login_page_con_json.locator_products)
        #assert "asd" in products_text, f"Se esperaba 'Products' en el texto, pero se obtuvo: {products_text}"



