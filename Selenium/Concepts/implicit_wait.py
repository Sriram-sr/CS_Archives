from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

#driver.implicitly_wait(5) #This will be applicable to all the below statements

driver.maximize_window()

#driver.get('http://www.expedia.com/')

#driver.find_element_by_xpath('//*[@id="wizardMainRegionV2"]/div/div/div/div/ul/li[2]/a').click()
#sleep(5)
#driver.find_element(By.ID,'<id>').click() #If ID given you can use this 

driver.get("http://www.automationpractice.com/")

#driver.find_element_by_name("search_query").send_keys("shirt")
#driver.find_element_by_name("submit_search").click()

#driver.find_element(By.ID,"search_query_top").send_keys("tops") #If ID given you can use this 
#driver.find_element(By.NAME,"submit_search").click()

#To click tab women and wait for a check box to appear,

driver.find_element(By.XPATH,"//*[@id='block_top_menu']/ul/li[1]/a").click()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver,5)
element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layered_category_4"]')))
element.click()
sleep(3)
driver.quit()
