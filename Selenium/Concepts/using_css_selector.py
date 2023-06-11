from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.facebook.com')

# Finding the element by constructing the css selector using tag name and id
# here the tag name is input and id is email

# driver.find_element(By.CSS_SELECTOR,'input#email').send_keys('Hello')

# constructing the css selector using only id (put #)

# driver.find_element(By.CSS_SELECTOR,'#email').send_keys('World')

# constructing using the tag and class combination 
# here the class is 'inputtext _55r1 _6luy' and tag is input (take the space out)

# driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys('user')

# To construct css selector only using class (put .)

# driver.find_element(By.CSS_SELECTOR,'.inputtext').send_keys('user')

# To construct css using tag name and any other attribute 
# Have to specify attribute along with the value

driver.find_element(By.CSS_SELECTOR,'input[data-testid=royal_email]').send_keys('fish')
# without tage also we can write the above only with brackets

# To construct using tag,class and any attribute

driver.find_element(By.CSS_SELECTOR,'input.inputtext[data-testid=royal_pass]').send_keys('duck')
# here both input boxes have same tage and class so differenciate with any other attribute







