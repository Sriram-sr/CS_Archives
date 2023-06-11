from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.maximize_window()

driver.get('https://www.globalsqa.com/demo-site/frames-and-windows/')

driver.implicitly_wait(5)

driver.find_element(By.ID,'iFrame').click()

sleep(4)

driver.switch_to.frame('globalSqa')  # Switching to frame after clicking iframe in page

all_element = driver.find_element(By.XPATH,'//*[@id="current_filter"]')  # selecting 'All' which is a drop down

click_element = driver.find_element(By.XPATH,'//*[@id="filter_list"]/li[2]/div')  #Selecting performance testing in that drop down

from selenium.webdriver import ActionChains

action = ActionChains(driver)

action.move_to_element(all_element).move_to_element(click_element).click().perform()

driver.switch_to.default_content()

nxt_element = driver.find_element(By.ID,'menu-item-2806')
nxt_element.click()