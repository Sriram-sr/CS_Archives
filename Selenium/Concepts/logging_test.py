from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')
driver.get('http://www.facebook.com')

username_element = driver.find_element_by_name('email')
#print(element.is_displayed())  #Searching for a box for entering email if displayed in webpage prints True
#print(element.is_enabled())  #If enabled prints True
password_element = driver.find_element_by_name('pass')

username_element.send_keys('8428259394')
password_element.send_keys('9600pdsv')

driver.find_element_by_name('login').click()
