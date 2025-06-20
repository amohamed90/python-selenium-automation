from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")

@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN)).click()
    sleep(10)