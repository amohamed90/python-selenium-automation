from selenium.webdriver.common.by import By
from pages.base_page import Page

class TermsAndConditions(Page):
    url = 'terms-conditions'

    def verify_terms_and_conditions_page(self):
        self.wait_for_url_contains(self.url)
