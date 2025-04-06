from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target main page")
def open_target_main_page(context):
    context.driver.get("https://www.target.com/")

@when("Click on Cart icon")
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]').click()
    sleep(5)

@then('Verify “Your cart is empty” message is shown')
def verify_results(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    expected_result = 'Your cart is empty'
    assert expected_result in actual_result, f'{expected_result} text not found in {actual_result}'

@when("Main click sign in")
def main_click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/AccountLink"]').click()
    sleep(5)

@when("Navigation click Sign In")
def navigation_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()
    sleep(5)

@then("Verify Sign In form opened")
def verify_results(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    expected_result = 'Sign in or create account'
    assert expected_result in actual_result, f'{expected_result} text not found in {actual_result}'