from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):

    USERNAME_FIELD = (By.ID, "username")
    PWD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    TERMS_AND_CONDITIONS_LINK = (By.CSS_SELECTOR, '[aria-label*="terms & conditions"]')

    username = 'rayyatkomxezx@murahpanel.com'
    password = '*********'

    def signing_in(self):
        self.find_element(*self.USERNAME_FIELD)

    def user_name_input(self):
        self.input_text(self.username, *self.USERNAME_FIELD)

    def continue_signing_in(self):
        self.click(*self.LOGIN_BUTTON)

    def pwd_input(self):
        self.input_text(self.password, *self.PWD_FIELD)

    def click_target_terms_and_conditions_link(self):
        self.click(*self.TERMS_AND_CONDITIONS_LINK)
