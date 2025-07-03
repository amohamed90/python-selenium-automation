from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

@then('Verify Privacy Policy Page opened')
def privacy_policy_page(context):
    context.app.privacy_policy_page.verify_privacy_policy_opened()

@then('Close current page')
def close_privacy_policy_window(context):
    context.app.privacy_policy_page.close_privacy_policy_window()