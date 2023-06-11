from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/kali/Github_Repo/Selenium/chromedriver.exe')
driver.get('http://testautomationpractice.blogspot.com/')

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()  #To click a alert button in webpage 
sleep(3)

#After getting the alert pop up

# driver.switch_to.alert.dismiss()
driver.switch_to.alert.accept()
