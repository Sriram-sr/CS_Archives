from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path= '/home/kali/Downloads/geckodriver')

driver.get(' https://phptravels.com/demo/')

# Task is to just move to element named company and it shows a menu and to slect blog element
company = driver.find_element(By.XPATH,'/html/body/header/div/nav/div[3]/span')
blog = driver.find_element(By.XPATH,'/html/body/header/div/nav/div[3]/div/a[1]')
Action = ActionChains(driver)

Action.move_to_element(company).move_to_element(blog).click().perform()
