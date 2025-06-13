from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on cart icon')
def click_cart_icon(context):
    # find element and click
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartIcon"]').click()

@then('Verify cart is empty')
def verify_cart_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

@then('Verify cart has items')
def verify_item(context):
    cart_items = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="cartItem"]')
    assert len(cart_items) > 0, f'Error, expected at least one cart item'
