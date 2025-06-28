from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    SEARCH_FIELD = (By.ID, 'search')
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
    SIGN_ACCT_BTN = (By.ID, 'account-sign-in')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart_icon(self):
        self.wait_for_element_visibility(*self.CART_ICON)
        self.wait_for_element_to_click(*self.CART_ICON)
        # self.click(*self.CART_ICON)

    def click_btn_account(self):
        self.click(*self.SIGN_ACCT_BTN)
