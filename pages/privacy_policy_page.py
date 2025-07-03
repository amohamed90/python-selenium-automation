from pages.base_page import Page

class PrivacyPolicyPage(Page):
    URL_PARTIAL_TEXT = 'target-privacy-policy'

    def verify_privacy_policy_opened(self):
        self.wait_for_url_contains(self.URL_PARTIAL_TEXT)

    def close_privacy_policy_window(self):
        self.close_window()