from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.techwithtim.net/')

search_box = driver.find_element_by_name('s')  # To find the search box
search_box.send_keys('test')
search_box.send_keys(Keys.RETURN)  # To enter word to search after that click enter

# main is the html tag under which all of the text located
# To wait for main to loaded we use Explicit wait

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait_object = WebDriverWait(driver,10)
main = wait_object.until(EC.presence_of_element_located((By.ID,'main'))) #EC.method((takes tuple))
print(main.text)  # This will print the whole content

articles = main.find_elements(By.TAG_NAME,'articles')
