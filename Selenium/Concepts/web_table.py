from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('https://www.techlistic.com/p/demo-selenium-practice.html')

# //*[@id="customers"]/tbody/tr[1]/th[1]
#//*[@id="customers"]/tbody/tr[1]/th[3]
#//*[@id="customers"]/tbody/tr[3]/td[1]  This is how the xpath shows as third row 1st column 

no_of_rows = len(driver.find_elements(By.XPATH,'//*[@id="customers"]/tbody/tr'))
no_of_cols = len(driver.find_elements(By.XPATH,'//*[@id="customers"]/tbody/tr[1]/th'))

print(no_of_rows)
print(no_of_cols)

row_1_elements = driver.find_elements(By.XPATH,'//*[@id="customers"]/tbody/tr[1]/th') #use th or tr for column
for i in row_1_elements :  #To find the row 1 values copy the xpath of row 1 and leave th alone and tr as 1
    print(i.text)


# value = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[2]/td[3]').text
# print(value)
# for r in range(1,no_of_rows+1):
#     for c in range(1,no_of_cols+1):
#         value = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[+r+]/td[+c+]').text
#         print(value)
       
# print(table)        