from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
ORDER_PICK_UP_BTN = (By.CSS_SELECTOR, "[data-test='shippingButton']")
CART_ICON = (By.CSS_SELECTOR, "[href='/cart']")
SEARCH_RESULTS = (By.XPATH, "//div[@data-test='lp-resultsCount']")
SIDE_BAR_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
PRODUCT_NAMES_RESULTS = (By.CSS_SELECTOR, '[data-test="product-title"]')
PRODUCT_NAME_DEALS = (By.CSS_SELECTOR, '[data-test="productCardVariantRecommendationTitle"]')
PRODUCT_NAME_POPULAR_FILTER = (By.CSS_SELECTOR, '[data-test="navItemTitleComponent"]')
PRODUCT_PRIMARY_IMAGES = (By.CSS_SELECTOR, '[data-test*="ProductCardImage/primary"]')
PRODUCT_POPULAR_IMAGES = (By.CSS_SELECTOR, '[class*="itemPictureWrapper"]')


@when('Add to cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_BAR_PRODUCT_NAME), message='name of product not showing')

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_BAR_PRODUCT_NAME).text
    print('Product Name is, ', context.product_name)

@when('Add to cart button from side-nav')
def add_to_cart_from_side_nav(context):
    context.driver.wait.until(EC.element_to_be_clickable(ORDER_PICK_UP_BTN), message='add to cart is not clickable').click()


@when('Open cart page')
def open_cart(context):
    context.driver.find_element(*CART_ICON).click()


@then("Verify {product} results show")
def verify_search(context, product):
    actual_result = context.driver.find_element(*SEARCH_RESULTS).text.lower()
    assert product in actual_result, f'Expected {product} to be in {actual_result}'

@then("Verify {product} name")
def verify_product_name(context, product):
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_NAMES_RESULTS), message=f'{product} main result is not showing')
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_NAME_DEALS), message=f'{product} name in deals is not showing')
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_NAME_POPULAR_FILTER), message=f'{product} name in popular filters is not showing')


@then('Verify {product} image')
def verify_product_image(context, product):
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_PRIMARY_IMAGES), message=f'{product} primary images do not show')
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_POPULAR_IMAGES), message=f'{product} popular images do not show')




