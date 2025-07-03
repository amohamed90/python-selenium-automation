from pages.main_page import MainPage
from pages.header_page import Header
from pages.search_results_page import SearchResultsPage
from pages.cart_page import Cart
from pages.side_menu_page import SideMenuPage
from pages.sign_in_page import SignInPage
from pages.target_app_page import TargetAppPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.terms_and_conditions_page import TermsAndConditions

class Application:

    def __init__(self, driver):
        self.header_page = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = Cart(driver)
        self.side_menu_page = SideMenuPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.terms_and_conditions_page = TermsAndConditions(driver)

