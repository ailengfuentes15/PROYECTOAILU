from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import json

class LoginPage(BasePage):

    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//input[@id='login-button']")


    #login_data= "login.json"

    def login_data(self):
        return self.get_data("login.json")

    def enter_username(self):
        get_username = self.get_data(self.login_data)
        username_value = get_username["username"]
        self.input_text(self.username, username_value)

    def enter_password(self):
        get_password = self.get_data(self.login_data)
        password_value = get_password["password"]
        self.input_text(self.password, password_value)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()