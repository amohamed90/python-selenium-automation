from selenium.webdriver.common.by import By
from behave import when, then

SIGN_IN_BTN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
USERNAME_FIELD = (By.ID, "username")

@when('Click on Sign in')
def click_sign_in(context):
    context.app.side_menu_page.click_sign_in_side_menu()


@then('Verify Sign in form opened')
def sign_in(context):
    context.driver.find_element(*USERNAME_FIELD)