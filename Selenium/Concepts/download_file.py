from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('http://demo.automationtesting.in/FileDownload.html')

driver.find_element(By.ID,'textbox').send_keys('Hello world')  #GIving text to the empty box
driver.find_element(By.ID,'createTxt').click() #Clicking generate file
#driver.find_element(By.ID,'link-to-download').click() #Clicking download file