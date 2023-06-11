# Task is to return all links in footer portion of the page
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demo.nopcommerce.com/')

all_links = driver.find_elements(By.XPATH,'//div[@class="footer"]//a')
print(len(all_links))
for link in all_links :
    print(link.text)

driver.close()