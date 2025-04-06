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

# open the url
driver.get('https://www.amazon.com/')

# CSS by ID => #
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
# CSS by ID and  tag => # and input
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
# CSS by class
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag")
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag.icp-nav-flag-us")
# CSS by class and tag
driver.find_element(By.CSS_SELECTOR, "span.icp-nav-flag")
# CSS by attribute => []
driver.find_element(By.CSS_SELECTOR, "[aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[name='field-keywords']")
driver.find_element(By.CSS_SELECTOR, "[aria-label='Search Amazon'][name='field-keywords']")
driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input.nav-input[name='field-keywords']")
# CSS, attribute, contains => *= []
driver.find_element(By.CSS_SELECTOR, "[aria-label*='Amazon']")
driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsBaseButton'][class*='h-margin-b-default']")