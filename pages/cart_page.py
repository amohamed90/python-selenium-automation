from pages.base_page import Page
from selenium.webdriver.common.by import By

class Cart(Page):

    EMPTY_CART = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def verify_cart_empty(self):
        self.find_element(*self.EMPTY_CART)