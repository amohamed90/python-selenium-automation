from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    SIDE_BAR_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
    ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
    ORDER_PICK_UP_BTN = (By.CSS_SELECTOR, "[data-test='shippingButton']")
    CART_ICON = (By.CSS_SELECTOR, "[href='/cart']")

    def verify_search_results(self, product):
        self.verify_partial_text(product,*self.SEARCH_RESULTS)

    def wait_for_element(self):
        self.wait_for_element_visibility(*self.SIDE_BAR_PRODUCT_NAME)

    def add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART)

    def store_product_info(self):
        return self.get_text(*self.SIDE_BAR_PRODUCT_NAME)

    def add_to_cart_side_nav(self):
        self.wait_for_element_to_click(*self.ORDER_PICK_UP_BTN)

    def open_cart(self):
        self.click(*self.CART_ICON)

