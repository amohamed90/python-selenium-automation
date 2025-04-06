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

# Open url
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%2F%3F_encoding%3DUTF8%26hvadid%3D694878214743%26hvdev%3Dc%26hvdvcmdl%3D%26hvexpln%3D67%26hvlocint%3D%26hvlocphy%3D9031992%26hvnetw%3Dg%26hvocijid%3D10712048830082493938--%26hvpone%3D%26hvpos%3D%26hvptwo%3D%26hvqmt%3Db%26hvrand%3D10712048830082493938%26hvtargid%3Dkwd-419491829174%26hydadcr%3D26642_11751832%26ie%3DUTF8%26index%3Daps%26keywords%3Dnew%2520account%2520sign%2520up%2520for%2520amazon%26mcid%3D453ce6308aa03548916f769835b7da28%26ref%3Dpd_sl_8lgzans1wq_b_p67%26tag%3Dgooghydr-20%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon-logo')

# Create Account Text
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your Name input field
driver.find_element(By.ID, 'ap_customer_name')

# Mobile Number or input field
driver.find_element(By.ID, 'ap_email')

# Password input field
driver.find_element(By.ID, 'ap_password')

# Password Requirement
driver.find_element(By.ID, 'auth-password-requirement-info')

# Re-enter Password Input field
driver.find_element(By.ID, 'ap_password_check')

# Button for creating the account
driver.find_element(By.ID, 'continue')

# Conditions of use
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'nodeId=508088')]")

# Privacy Notice
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'nodeId=468496')]")

# Sign in link
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

print('Tests passed')

