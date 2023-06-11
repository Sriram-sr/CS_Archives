from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://admin-demo.nopcommerce.com/login')

email_input_box = driver.find_element(By.ID,'Email') 
text_in_box = email_input_box.get_attribute('value') # Finding what is already present in the emailbox
email_input_box.clear()
email_input_box.send_keys('myemailid@gmail.com')

password_input_box = driver.find_element(By.ID,'Password')
pass_text = password_input_box.get_attribute('type')
print(pass_text)
print(text_in_box)

login_button = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button')
print(login_button.text)  # This is a link element it will return any text present inside its tag

