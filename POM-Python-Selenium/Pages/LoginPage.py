from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """By Locators"""
    EMAIL = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='loginForm']/div/div/input")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign Up")

    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""
    """This Method Use to get the Page title"""

    def get_login_title(self, title):
        return self.get_title(title)

    """This e=method is use to check sugn up link is visible or not """
    def is_signUp_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """This method is use to login to application"""

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
