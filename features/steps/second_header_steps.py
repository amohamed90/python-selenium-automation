from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(5)