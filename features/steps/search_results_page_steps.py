from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Add to cart')
def add_to_cart(context):
    add_btn = context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
    sleep(4)
    add_btn.click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()

@then("Verify {product} results show")
def verify_search(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text.lower()
    assert product in actual_result, f'Expected {product} to be in {actual_result}'