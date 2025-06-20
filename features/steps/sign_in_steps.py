from selenium.webdriver.common.by import By
from behave import when, then

SIGN_ACCT_BTN = (By.ID, 'account-sign-in')
SIGN_IN_BTN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
USERNAME_FIELD = (By.ID, "username")

@when('Click on sign account')
def click_account(context):
    # find element and click
    context.driver.find_element(*SIGN_ACCT_BTN).click()

@when('Click on Sign in')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_BTN).click()


@then('Verify Sign in form opened')
def sign_in(context):
    context.driver.find_element(*USERNAME_FIELD)