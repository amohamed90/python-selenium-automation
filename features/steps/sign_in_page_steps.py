from time import sleep

from behave import when, then

@when('Verify Sign in form opened')
def sign_in(context):
    context.app.sign_in_page.signing_in()

@when('Enter username')
def enter_username(context):
    context.app.sign_in_page.user_name_input()

@when('Click continue')
def click_continue(context):
    context.app.sign_in_page.continue_signing_in()

@when('Enter password')
def enter_password(context):
    context.app.sign_in_page.pwd_input()

@when('Store original window')
def store_original_window(context):
    context.original_window_sign_in = context.app.sign_in_page.get_current_window_id()

@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_target_terms_and_conditions_link()

@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.sign_in_page.switch_to_window()