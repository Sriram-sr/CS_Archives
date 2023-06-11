from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get('https://www.techlistic.com/p/selenium-practice-form.html')

manual_tester_chcekbox = driver.find_element(By.CSS_SELECTOR,'input#profession-0')
print(manual_tester_chcekbox.is_selected())

manual_tester_chcekbox.click()
print(manual_tester_chcekbox.is_selected())
