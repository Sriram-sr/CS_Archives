from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('http://demo.automationtesting.in/Windows.html')

parent_window_name = driver.title

driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()

print(driver.current_window_handle)  #Prints the unique nmbr given to main window

window_handles = driver.window_handles  #Gives the list of unique numbers given to each windows 
sleep(3)

for window in window_handles :
    driver.switch_to.window(window)
    print(driver.title)
    if driver.title == parent_window_name :
        driver.close() #To close the parent window and only have the newly opened window

sleep(3)
#driver.quit() #To close both the windows    

//*[@id="customers"]/tbody/tr