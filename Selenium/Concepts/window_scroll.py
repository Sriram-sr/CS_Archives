from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.maximize_window()
driver.get('https://www.toolsqa.com/selenium-webdriver/scroll-element-view-selenium-javascript/')

#Scrolling down the page till pixel (1000)

driver.execute_script("window.scrollBy(0,1000)","")  #Javascript snippet
sleep(3)

#Scrolling down till the found element

#This will scroll upto stop value which is 'Previous page' in the website
Stop_Value = driver.find_element(By.XPATH,'/html/body/div[1]/div/section[3]/div/div[1]/div/div/div[2]/div/a/span')
driver.execute_script('arguments[0].scrollIntoView()',Stop_Value)

#Scrolling till end of the page

driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
