from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open target circle page')
def open_main(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

@then('Verify count of benefit cells')
def verify_benefit_cells(context):
    actual_count = context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content")
    assert len(actual_count) >= 10, f'{actual_count} is less than 10'