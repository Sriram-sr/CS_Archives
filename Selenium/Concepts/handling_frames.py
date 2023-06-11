from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('https://www.selenium.dev/selenium/docs/api/java/overview-summary.html')

driver.find_element_by_link_text('FRAMES').click()  #To click 'FRAMES' button which is in link form

driver.switch_to.frame('packageFrame')  # Found the frame name in <iframesrc tag as name = 'packageFrame'

driver.find_element_by_link_text('ActiveSession').click()  #Clicking the link in the frame switched
 
driver.switch_to.default_content()  #Cannot switch directly so returning back by switch to  default content

driver.switch_to.frame('packageListFrame')

driver.find_element_by_link_text('org.openqa.selenium.cli').click()

sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame('classFrame')

driver.find_element_by_link_text('DEPRECATED').click()