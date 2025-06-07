from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

url = 'https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=YJB074CTT738XF8TAZWX&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'

# open the url
driver.get(url)

# Even though I can find locators with ID, i will use CSS for this homework since it is all about CSS locators unless it can't be selected by CSS

# Locate Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon-logo')

# Locate Create account text
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
# OR use XPATH to get partial text
driver.find_element(By.XPATH, '//h1[contains(.,"Create account")]')

# Locate your name input field
# Optimal solution By.ID
driver.find_element(By.ID, 'ap_customer_name')
# OR using CSS locators
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
driver.find_element(By.CSS_SELECTOR,'[placeholder="First and last name"]' )

# Locate Mobile number or email
# Optimal locator is By.ID
driver.find_element(By.ID, 'ap_email')
# OR using CSS locators
driver.find_element(By.CSS_SELECTOR, '#ap_email')
driver.find_element(By.CSS_SELECTOR, '[data-validation-id="email"]')

# Locate Password
# Optimal locator is By.ID
driver.find_element(By.ID, 'ap_password')
# OR using css locators
driver.find_element(By.CSS_SELECTOR, '.auth-require-password-validation')

# Locate password content message
driver.find_element(By.CSS_SELECTOR, '#ap_password_context_message_section')

# Locate password check
# Optimal locator By.ID
driver.find_element(By.ID, 'ap_password_check')
# OR By css locators
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
driver.find_element(By.CSS_SELECTOR, '[name="passwordCheck"]')

# Locate Continue button link
# Optimal locator by ID
driver.find_element(By.ID, 'continue')
# OR by css locators
driver.find_element(By.CSS_SELECTOR, '#continue')
driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="auth-continue-announce"]')

# Locate Condition of Use lin
driver.find_element(By.CSS_SELECTOR, '[href*="ref=ap_register_notification_condition_of_use?')

# Locate Privacy Notice
driver.find_element(By.CSS_SELECTOR, '[href*="ref=ap_register_notification_privacy_notice"]')

# Locate Sign in link at the bottom
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')