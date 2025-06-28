from behave import given, when, then

@then('Verify cart is empty')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()

@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_cart_has_correct_product(context.product_name)

@then('Verify cart has items')
def verify_item(context):
    context.app.cart_page.verify_cart_has_items()

@then('Verify cart page opened')
def verify_cart_page(context):
    context.app.cart_page.verify_cart_opened()