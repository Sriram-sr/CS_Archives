from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('http://www.amazon.in')
print(driver.title)
print(driver.current_url)
#driver.find_element_by_xpath("//*[@id='nav-xshop']/a[5]").click() #clicking 'Electronics' element using xpath
driver.find_element(By.XPATH,"//*[@id='nav-xshop']/a[5]").click()
#driver.close() It closes current browser 
sleep(5)
driver.refresh()  # To refresh the page
driver.quit() #Closes all browsers

# If there is a element like a box and after finding that element
    # print(element.text) will print the content inside that 
