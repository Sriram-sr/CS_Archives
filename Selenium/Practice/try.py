from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")

print(driver.find_element_by_xpath("/html/body").text)