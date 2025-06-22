from selenium.webdriver.common.by import By
from behave import given, when, then

CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
EMPTY_CART = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
CART_WITH_ITEMS = (By.CSS_SELECTOR, '[data-test="cartItem"]')
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Click on cart icon')
def click_cart_icon(context):
    # find element and click
    context.app.cart_page.click_cart_icon()
    # context.driver.find_element(*CART_ICON).click()

@then('Verify cart is empty')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()
    # context.driver.find_element(*EMPTY_CART)

@then('Verify cart has correct product')
def verify_product_name(context):
    product_name_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    print('Name in cart is ', product_name_in_cart)
    assert product_name_in_cart[:20] == context.product_name[:20], f"Error, {context.product_name[:20]} didn't match {product_name_in_cart[:20]}"

@then('Verify cart has items')
def verify_item(context):
    cart_items = context.driver.find_elements(*CART_WITH_ITEMS)
    assert len(cart_items) > 0, f'Error, expected at least one cart item'
