from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select #For selecting the options of dropdown

driver = webdriver.Chrome('/home/sriram/Selenium/chromedriver')
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

drop = driver.find_element_by_id('RESULT_RadioButton-9')
option = Select(drop)

#By selecting with visible text
#option.select_by_visible_text('Evening')
sleep(3)

#By Selecting with index 
#option.select_by_index(2)
sleep(3)

#By selecting with value
#option.select_by_value('Radio-0')

#To find the number of options present
all_options = option.options
print(len(all_options))

#To capture all options and print
for each in all_options :
    print(each.text)
