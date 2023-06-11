from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# To write relative xpath
# //tagname[@attribute=value]  If no tag name put *

# driver.find_element_by_xpath('//input[@id="small-searchterms"]').send_keys('Hello')
# driver.find_element_by_xpath('//*[@id="small-searchterms"]').send_keys('Hello')
  # If you write the relative xpath like above will find the element by every tag with the attribute specified

# Using or with multiple attributes

driver.find_element(By.XPATH,"//input[@id='small-searchterms' or @name='q']").send_keys('Hello')
