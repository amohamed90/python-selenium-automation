from behave import given, when, then

@when('Search for {product}')
def search_product(context, product):
    context.app.header_page.search_product(product)

@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header_page.click_cart_icon()

@when('Click on sign account')
def click_account(context):
    context.app.header_page.click_btn_account()