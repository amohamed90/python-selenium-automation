from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
SEARCH_FIELD = (By.ID, 'search')

@when('Search for {product}')
def search_product(context, product):
    context.app.header_page.search_product(product)
    # context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # context.driver.find_element(*SEARCH_BTN).click()
    # context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN)).click()
    # sleep(10)

@when('Click on cart icon')
def click_cart_icon(context):
    # find element and click
    context.app.header_page.click_cart_icon()
    # context.driver.find_element(*CART_ICON).click()

@when('Click on sign account')
def click_account(context):
    # find element and click
    # context.driver.find_element(*SIGN_ACCT_BTN).click()
    context.app.header_page.click_btn_account()