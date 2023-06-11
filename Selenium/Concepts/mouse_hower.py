from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('https://opensource-demo.orangehrmlive.com/')

#logging in
driver.find_element(By.ID,'txtUsername').send_keys('Admin')
driver.find_element(By.ID,'txtPassword').send_keys('admin123')
driver.find_element(By.NAME,'Submit').click()

#Finding the three mousehower elements
admin = driver.find_element(By.XPATH,'//*[@id="menu_admin_viewAdminModule"]/b')
user_management = driver.find_element(By.ID,'menu_admin_UserManagement')
user = driver.find_element(By.ID,'menu_admin_viewSystemUsers')

from selenium.webdriver import ActionChains
#For moving the cursor over admin shows usrmngmnt shows user and then click
actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_management).click(user).perform()