from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Target Help Page')
def open_main(context):
    context.driver.get('https://help.target.com/help')

@then('Verify Target Help UI text')
def verify_target_help(context):
    actual_help_text = context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Target Help')]").text
    expected_text = 'Target Help'
    assert actual_help_text == expected_text, f'Error, {expected_text} != {actual_help_text}'

@then('Verify Target Help grids')
def verify_grids(context):
    grids = context.driver.find_elements(By.CSS_SELECTOR, ".boxSmall div")
    actual = []
    expected = [
        'track an order',
        'view current promotions',
        'pickup & delivery',
        'returns & receipts',
        'check GiftCard balance',
        'fix an issue'
    ]

    for grid in grids:
        actual.append(grid.text.strip())

    for grid in actual:
        if grid not in expected:
            assert False, f'Error, {grid} not in {expected}'

@then('Verify Manage My Text')
def verify_manage_me(context):
    expected_text = 'manage my'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "div.grid_6 h3").text
    assert actual_text == expected_text, f'Error, {actual_text} != {expected_text}'

@then('Verify Manage My Links')
def verify_manage_links(context):
    manage_links = context.driver.find_elements(By.CSS_SELECTOR, ".manageMy li")
    actual_links = []
    expected_links = [
        'Target.com account',
        'Target.com password',
        'Target Circle Card',
        'Target Circle account',
        'Gift Registry'
    ]

    for link in manage_links:
        actual_links.append(link.text.strip())

    for link in expected_links:
        if link not in actual_links:
            assert False, f'Error, {link} not in {expected_links}'


@then('Verify Contact Us Card')
def verify_contact_us(context):
    help_cards = context.driver.find_elements(By.CSS_SELECTOR, ".grid_4 h3")
    expected_card = 'contact us'
    contact_us_text = ''
    for card in help_cards:
        if card.text == expected_card:
            contact_us_text += card.text

    assert contact_us_text == expected_card, f'Error, {contact_us_text} != {expected_card}'


@then('Verify See Contact Options Link')
def verify_see_contact_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "[title='see contact options']")



@then('Verify Product Recalls Card')
def verify_product_recalls(context):
    help_cards = context.driver.find_elements(By.CSS_SELECTOR, ".grid_4 h3")
    expected_card = 'product recalls'
    contact_us_text = ''
    for card in help_cards:
        if card.text == expected_card:
            contact_us_text += card.text

    assert contact_us_text == expected_card, f'Error, {contact_us_text} != {expected_card}'


@then('Verify All Product recalls Link')
def verify_see_product_recall_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='commandLink']")

@then('Verify Browse All Help Pages Text exist')
def verify_browse_pages_text(context):
    expected_text = 'Browse all Help pages'
    actual_browse_text = context.driver.find_element(By.CSS_SELECTOR, "#divID1 h2").text

    assert expected_text == actual_browse_text, f'Error, {expected_text} != {actual_browse_text}'

@then('Verify Browse All Help Links')
def verify_browse_pages_links(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, ".accessLinks.bold")
    actual_links = []
    expected_links = [
        'Orders & Purchases',
        'Returns & Exchanges',
        'Promotions & Coupons',
        'Target Circle™',
        'Partner Programs',
        'Registries & Lists',
        'Delivery & Pickup',
        'Target Account',
        'Payment Options',
        'Gift Cards',
        'Product Support & Services',
        'Product Safety & Recalls',
        'Policies & Guidelines',
        'Compliance',
        'Other Services',
        'Nutrition Information',
        'Technical Support'
    ]

    for link in links:
        actual_links.append(link.text.strip())

    for link in actual_links:
        if link not in expected_links:
            assert False, f'Error, {link} not in {expected_links}'