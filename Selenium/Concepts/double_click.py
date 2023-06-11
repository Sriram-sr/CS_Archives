from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()

from selenium.webdriver import ActionChains

element = driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')

actions = ActionChains(driver)
sleep(3)
actions.double_click(element).perform()