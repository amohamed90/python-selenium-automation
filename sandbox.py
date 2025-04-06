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


# # Find an element and enter a text
# driver.find_element(By.ID, 'search').send_keys('tea')
# driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#
# # Clear first text input text
# # sleep(2)
# # driver.find_element(By.ID, 'search').clear()
#
# #Enter another search text
# # driver.find_element(By.ID, 'search').send_keys('coffee')
#
# sleep(5)
#
# # Verification
# # By finding 1 element
# # driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']")
# # print('Test case passed')
#
# #By finding text
# actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
# expected_text = 'tea'
#
#
#
# print(f'Actual Text: {actual_text}')
#
# assert expected_text in actual_text.lower(), f'Error, {expected_text} is not in {actual_text}'
# print('Test case passed')
#
# sleep(10)