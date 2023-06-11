from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/home/sriram/Selenium/chromedriver')
driver.maximize_window()

driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source_element = driver.find_element_by_id('box6')  #Element to be moved
target_element = driver.find_element_by_id('box107')  #Element moving location

from selenium.webdriver import ActionChains

action = ActionChains(driver)

action.drag_and_drop(source_element,target_element).perform()