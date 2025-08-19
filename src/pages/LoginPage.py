from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//input[@id='login-button']")

    login_data= "login.json"

def __init__(self, driver):
        """Inicializa la clase LoginPage con una instancia de WebDriver."""
        super().__init__(driver)
        self.driver = driver

def navigate_to_login_page(self, url):
    get_url = self.get_data(self.login_data)
    url_value = get_url["url"]
    self.navigate_to(url_value)  # Usa el parámetro URL

def enter_username(self, username):
    get_username = self.get_data(self.login_data)
    username_value = get_username["username"]
    self.input_text(self.username_input, username_value)


def enter_password(self, password):
    get_password = self.get_data(self.login_data)
    password_value = get_password["password"]
    self.input_text(self.password_input, password_value)

def click_login_button(self):
    self.click_element(self.login_button)