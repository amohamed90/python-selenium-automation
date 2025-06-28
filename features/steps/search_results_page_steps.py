from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRODUCT_NAMES_RESULTS = (By.CSS_SELECTOR, '[data-test="product-title"]')
PRODUCT_NAME_DEALS = (By.CSS_SELECTOR, '[data-test="productCardVariantRecommendationTitle"]')
PRODUCT_NAME_POPULAR_FILTER = (By.CSS_SELECTOR, '[data-test="navItemTitleComponent"]')
PRODUCT_PRIMARY_IMAGES = (By.CSS_SELECTOR, '[data-test*="ProductCardImage/primary"]')
PRODUCT_POPULAR_IMAGES = (By.CSS_SELECTOR, '[class*="itemPictureWrapper"]')


@when('Add to cart')
def add_to_cart(context):
    context.app.search_results_page.add_to_cart_btn()
    context.app.search_results_page.wait_for_element()

@when('Store product name')
def store_product_name(context):
    context.product_name = context.app.search_results_page.store_product_info()
    print('Product Name is, ', context.product_name)

@when('Add to cart button from side-nav')
def add_to_cart_from_side_nav(context):
    context.app.search_results_page.add_to_cart_side_nav()

@when('Open cart page')
def open_cart(context):
    context.app.search_results_page.open_cart()


@then("Verify {product} results show")
def verify_search(context, product):
    context.app.search_results_page.verify_search_results(product)


@then("Verify {product} name")
def verify_product_name(context, product):
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_NAMES_RESULTS), message=f'{product} main result is not showing')
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_NAME_DEALS), message=f'{product} name in deals is not showing')
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_NAME_POPULAR_FILTER), message=f'{product} name in popular filters is not showing')


@then('Verify {product} image')
def verify_product_image(context, product):
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_PRIMARY_IMAGES), message=f'{product} primary images do not show')
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_POPULAR_IMAGES), message=f'{product} popular images do not show')




