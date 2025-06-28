from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    SEARCH_FIELD = (By.ID, 'search')
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')

    def search_product(self):

        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)