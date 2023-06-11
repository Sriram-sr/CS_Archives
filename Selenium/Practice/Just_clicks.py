from selenium import webdriver

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')
driver.maximize_window()
driver.get('https://www.businessinsider.in/tech/enterprise/news/why-companies-are-flocking-to-the-cloud-more-than-ever/articleshow/81008976.cms#:~:text=Moving%20to%20the%20cloud%20can,to%20Woo%20and%20other%20experts.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# waiting for a element all in the top of the page like a mouse hower element
element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mainnav"]/ul/li[1]/div/div/ul/li[9]/a')))

element.click()

driver.find_element_by_xpath('//*[@id="nav-desktop-menu"]/div/div/div/div/div/div/div/div/div[4]/div[1]/ul/li[1]/a').click()

