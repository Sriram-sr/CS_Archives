from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://192.168.0.102:4000/')

# To scroll the screen to required position
driver.execute_script("window.scrollBy(0,2000)","")

sign_up_element = driver.find_element(By.XPATH,'//*[@id="root"]/nav/div/ul/li[4]/a')
sign_up_element.click()

sleep(5)
click_sign_up = driver.find_element(By.LINK_TEXT,'Start Now')
click_sign_up.click()

def filling_signup():
    driver.find_element(By.NAME,'component-error').send_keys('hello')
    driver.find_element(By.NAME,'lastname').send_keys('world')
    driver.find_element(By.NAME,'mobileNumber').send_keys('9884430239')
    driver.find_element(By.NAME,'emailId').send_keys('sriramsr9090@gmail.com')
    driver.find_element(By.NAME,'password').send_keys('Sriram@1234')
    driver.find_element(By.NAME,'confirmpassword').send_keys('Sriram@1234')
    driver.find_element(By.NAME,'submitButton').click()
filling_signup()    
