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

# # open the url
# driver.get('https://www.target.com/')
#
# # Click the signin button
# driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
#
# # Click signin from side navigation
# driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
#
# # Verify Signin page opened > “Sign into your Target account” text is shown
# driver.find_element(By.XPATH, "//span[text() ='Sign into your Target account']")
#
# # Verify Signin page opened > SignIn button is shown
# driver.find_element(By.ID, 'login')
#
# print('Tests passed')

#####################################################################################

# open the url
driver.get('https://www.target.com/')

# click on 'Account' button
driver.find_element(By.ID, 'account-sign-in').click()
sleep(5)

# click on the sign-in btn from the side navigation
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(5)

# verify sign-in page opened
driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']")

# sign-in btn is shown
driver.find_element(By.ID, 'login')

print('test passed')