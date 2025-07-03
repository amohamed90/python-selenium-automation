from behave import given, when, then

@given('Open Target App page')
def open_target_app_page(context):
    context.app.target_app_page.open_target_app()

@given('Store original window')
def store_window(context):
    context.original_window = context.app.target_app_page.get_current_window_id()

@when('Click Privacy Policy link')
def click_privacy_policy(context):
    context.app.target_app_page.click_privacy_policy()

@when('Switch to new window')
def switch_to_new_window(context):
    context.app.target_app_page.switch_to_window()

@then('Return to original window')
def return_original_window(context):
    context.app.target_app_page.switch_to_window_by_id(context.original_window)
