from selenium import webdriver

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')

driver.get('http://www.facebook.com/')

driver.save_screenshot('/home/sriram/Selenium/new_screenshot.png')

driver.close()