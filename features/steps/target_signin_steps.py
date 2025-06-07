from selenium.webdriver.common.by import By
from behave import when, then


@when('Click on sign account')
def click_account(context):
    # find element and click
    context.driver.find_element(By.ID, 'account-sign-in').click()

@when('Click on Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()


@then('Verify Sign in form opened')
def sign_in(context):
    context.driver.find_element(By.ID, "username")