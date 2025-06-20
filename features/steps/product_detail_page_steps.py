from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRODUCT_COLOR = (By.CSS_SELECTOR, '[aria-label*="Color"]')
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='headerWrapper']")


@given('Open target {product_id} detailed page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/{product_id}')

@then('User can click through colors')
def product_colors(context):
    expected_colors = ['Navy Denim', 'Dark Wash', 'Light Wash']
    actual_colors = []
    context.driver.wait.until(EC.presence_of_element_located(PRODUCT_COLOR))

    colors = context.driver.find_elements(*PRODUCT_COLOR)

    for color in colors:
        color.click()
        current_color = context.driver.find_element(*SELECTED_COLOR).text
        current_color = current_color.split('\n')[1]
        actual_colors.append(current_color)

    for actual_color in actual_colors:
        assert actual_color in expected_colors, f'{actual_color} not found in {expected_colors}'


