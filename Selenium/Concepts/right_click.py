from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/home/sriram/Selenium/chromedriver')

driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

#This button is for right click so it wont show inspect option use f12\
#     to get html code and locate the element
element = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')

from selenium.webdriver import ActionChains
action = ActionChains(driver)

action.context_click(element).perform() #This will perform right click

driver.find_element_by_xpath('/html/body/ul/li[4]').click() #To click paste option present in the previous action