from pages.main_page import MainPage
from pages.header_page import Header
from pages.search_results_page import SearchResultsPage
from pages.cart_page import Cart
from pages.side_menu_page import SideMenuPage
from pages.sign_in_page import SignInPage

class Application:

    def __init__(self, driver):
        self.header_page = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = Cart(driver)
        self.side_menu_page = SideMenuPage(driver)
        self.sign_in_page = SignInPage(driver)

