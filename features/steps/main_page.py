from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')