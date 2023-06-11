from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome('/home/sriram/Selenium/chromedriver')
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#Working with radio boxes
status = driver.find_element(By.ID,'RESULT_RadioButton-7_0').is_selected()
print(status)

#driver.find_element(By.ID,'RESULT_RadioButton-7_0').click()
#print(driver.find_element(By.ID,'RESULT_RadioButton-7_0').is_selected())

#button = driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label")
#driver.execute_script("arguments[0].click();", button) #To_Click different method
sleep(3)
radio_button = driver.find_element(By.ID,'RESULT_RadioButton-7_1')
driver.execute_script('arguments[0].click()',radio_button) #Selecting female in the site
print(driver.find_element(By.ID,'RESULT_RadioButton-7_1').is_selected())

#Working with checkboxes

check_box = driver.find_element(By.ID,'RESULT_CheckBox-8_0')
driver.execute_script('arguments[0].click()',check_box) #Selecting sunday in site
check_box_sat = driver.find_element(By.ID,'RESULT_CheckBox-8_6')
driver.execute_script('arguments[0].click()',check_box_sat)