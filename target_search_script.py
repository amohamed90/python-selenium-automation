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
driver.get('https://www.target.com/')

# Get the search input element and look for an item
driver.find_element(By.ID, 'search').send_keys('Water')

# Click on the Search button
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)
# Verify that the page returned relevant results
actual_result = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
expected_result = 'water'

assert expected_result in actual_result.lower(), f'{expected_result} not found in {actual_result}'

print('Test case passed')
