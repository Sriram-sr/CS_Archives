from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/home/sriram/Selenium/chromedriver')
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#To find the links present in the website 

#links = driver.find_element(By.TAG_NAME,'a')
# links = driver.find_elements_by_tag_name("a")
# print(len(links))

# for link in links :
#     print(link.text)

#To click the links in the webpage 

driver.find_element(By.LINK_TEXT,'Software Testing Tutorials').click()    
# driver.find_element(By.PARTIAL_LINK_TEXT,'Software').click()    #To click the link if half of the link text is given
