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

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-search-submit-button')

# By XPath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@role='searchbox']")

# By XPath multiple attributes
driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords' and @role='searchbox']")

# By XPath with any tag
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']")

# By XPath using text
driver.find_element(By.XPATH, "//h2[text()='Spring break styles for all']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# By XPath using contains
driver.find_element(By.XPATH, "//h2[contains(text(), 'Spring break styles for all')]")
driver.find_element(By.XPATH, "//select[contains(@class, 'nav-search-dropdown')]")

# By XPath using partial text match
driver.find_element(By.XPATH, "//h2[contains(text(), 'Spring break)]")