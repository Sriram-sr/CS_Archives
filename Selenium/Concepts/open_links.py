from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('https://www.techwithtim.net/')

element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,'Python Programming')))

element.click()