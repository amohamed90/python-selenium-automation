from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
SEARCH_FIELD = (By.ID, 'search')

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product()
    # context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # context.driver.find_element(*SEARCH_BTN).click()
    # context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN)).click()
    # sleep(10)