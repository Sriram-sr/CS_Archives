from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
driver.maximize_window()

# Finding the password box element by using contains method of xpath
time.sleep(5)
# Here 'input' is a tag name id is 'pass'
# password = driver.find_element(By.XPATH,"//input[contains(@id,'pass')]")

# Finding element using starts-with function in xpath
password = driver.find_element(By.XPATH,"//input[starts-with(@name,'pas')]")
password.send_keys('Hkhdg')

driver.close()


