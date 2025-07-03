from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page

class SideMenuPage(Page):
    SIGN_IN_BTN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    GREET_TEXT = (By.CSS_SELECTOR, '[data-test="modal-drawer-heading"]')
    greeting = 'Hi'

    def click_sign_in_side_menu(self):
        self.click(*self.SIGN_IN_BTN)
        # sleep(10)

    def verify_user_signed_in(self):
        self.verify_partial_text(self.greeting, *self.GREET_TEXT)