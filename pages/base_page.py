from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def item_has_count(self, *locator):
        actual_count = self.driver.find_elements(*locator)
        assert len(actual_count) > 0, f'Error, expected at least one cart item'

    def wait_for_element_to_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator), message='element is not clickable').click()

    def wait_for_element_visibility(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator), message='Element does not exist')

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element_located(locator), message='Element is still visible')

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text[:20] == expected_text[:20], f'{actual_text} does not match {expected_text}'

    def verify_partial_text(self, partial_text, *locator):
        actual_text = self.find_element(*locator).text
        assert partial_text in actual_text, f'{partial_text} not in {actual_text}'

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f'{actual_url} does not match {expected_url}'

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, f'{expected_partial_url} is not in {actual_url}'

    def wait_for_url_contains(self, partial_url):
        self.wait.until(EC.url_contains(partial_url), message=f'{partial_url} does not exist')