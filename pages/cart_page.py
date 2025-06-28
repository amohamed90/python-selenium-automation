from pages.base_page import Page
from selenium.webdriver.common.by import By


class Cart(Page):

    EMPTY_CART = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    CART_WITH_ITEMS = (By.CSS_SELECTOR, '[data-test="cartItem"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    expected_text = 'Your cart is empty'
    # expected_url = 'https://www.target.com/cart'
    expected_url = '/cart'

    def verify_cart_empty(self):
        self.verify_text(self.expected_text,*self.EMPTY_CART)

    def verify_cart_opened(self):
        self.wait_for_url_contains(self.expected_url)

    def verify_cart_has_items(self):
        return self.item_has_count(*self.CART_WITH_ITEMS)

    def verify_cart_has_correct_product(self, expected_text):
        self.verify_text(expected_text,*self.PRODUCT_NAME)