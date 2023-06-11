from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://automationpractice.com/index.php')

# clicking a element having text as 'Women' and tag name 'a'

women = driver.find_element(By.XPATH,"//a[text()='Women']")
women.click()