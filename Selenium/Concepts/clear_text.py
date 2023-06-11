from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://admin-demo.nopcommerce.com/login')

email_input_box = driver.find_element(By.ID,'Email')
current_text_in_box = email_input_box.get_attribute('value') # getting the value currently present in the text box
email_input_box.clear() # clearing the data present 
sleep(5)

email_input_box.send_keys(current_text_in_box) # passing the same data




