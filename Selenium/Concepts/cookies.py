from selenium import webdriver

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('http://www.amazon.in/')

cookies = driver.get_cookies()
print(len(cookies))
#print(cookies)

# driver.delete_all_cookies()
new_cookie = {'name':'Mycookie','value':'123456'}  #You have to give the number also in string
driver.add_cookie(new_cookie)

cookies = driver.get_cookies()
print(len(cookies))

driver.delete_cookie('Mycookie')

cookies = driver.get_cookies()
print(len(cookies))

driver.close()