from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/home/sriram/Selenium/chromedriver')
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

input_boxes = driver.find_elements(By.CLASS_NAME,'text_field')
print(len(input_boxes))  #To find number of text boxes 

driver.find_element(By.NAME,'RESULT_TextField-1').send_keys('SRI')
driver.find_element(By.NAME,'RESULT_TextField-2').send_keys('RAM')

print(driver.find_element_by_name('RESULT_TextField-1').is_displayed()) #To check if the check box is displayed or not
print(driver.find_element_by_name('RESULT_TextField-1').is_enabled())

