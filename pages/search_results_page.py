from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search_results(self):
        actual_result = self.find_element(*self.SEARCH_RESULTS).text.lower()
        assert 'tea' in actual_result, f'Expected tea to be in {actual_result}'
