from time import sleep

from behave import given, when, then

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.terms_and_conditions_page.verify_terms_and_conditions_page()

@then('User can close new window')
def close_window(context):
    context.app.terms_and_conditions_page.close_window()

@then('switch back to original')
def switch_back_to_original_window(context):
    context.app.terms_and_conditions_page.switch_to_window_by_id(context.original_window_sign_in)
    sleep(5)