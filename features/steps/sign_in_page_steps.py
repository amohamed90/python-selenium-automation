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
