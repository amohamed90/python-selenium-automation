from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_cart_icon(context):
    # find element and click
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartIcon"]').click()


@then('Verify cart is empty')
def verify_cart_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')