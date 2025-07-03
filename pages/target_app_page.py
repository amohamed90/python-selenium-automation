from selenium.webdriver.common.by import By
from pages.base_page import Page

class TargetAppPage(Page):

    PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, '[aria-label*="privacy policy"]')

    def open_target_app(self):
        self.driver.get('https://www.target.com/c/target-app/-/N-4th2r')

    def click_privacy_policy(self):
        self.click(*self.PRIVACY_POLICY_LINK)