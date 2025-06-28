from behave import when, then

@when('Click on Sign in')
def click_sign_in(context):
    context.app.side_menu_page.click_sign_in_side_menu()

@then('Verify user is signed in')
def verify_user_is_signed_in_verification(context):
    context.app.side_menu_page.verify_user_signed_in()