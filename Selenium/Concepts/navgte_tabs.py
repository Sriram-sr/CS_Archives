from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('http://www.google.com')
print(driver.title)
sleep(3)

driver.get('http://www.facebook.com')
print(driver.title)
sleep(3)

driver.back()
print(driver.title)
sleep(3)

driver.forward()
print(driver.title)
