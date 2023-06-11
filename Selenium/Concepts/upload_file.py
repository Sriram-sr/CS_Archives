from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.maximize_window()

driver.get('https://testautomationpractice.blogspot.com/')

driver.switch_to.frame('frame-one1434677811') #Switch to frame using frame ID 

driver.find_element_by_id('RESULT_FileUpload-10').send_keys('/home/sriram/txtf.txt')

from selenium.webdriver.support.ui import Select 

driver.switch_to.default_content() # To back to the default frame which is at the left of the page
sleep(2)
drop_down_element = driver.find_element(By.ID,'animals')
option = Select(drop_down_element)
option.select_by_visible_text('Avatar')  #To click the option 

option_list = option.options

for each_option in option_list :
    print(each_option.text)