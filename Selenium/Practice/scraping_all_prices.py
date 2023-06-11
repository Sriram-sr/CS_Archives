from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')
driver.maximize_window()

driver.get('http://demostore.supersqa.com/')

# All products have a common class 'product'
all_products = driver.find_elements_by_class_name('product')

print(len(all_products))

# for i in all_products :
#     print(i.text)
final_dict = {}
for product in all_products :
    details_list = product.text.split()
    for each in details_list :
        if each[0] == '$' :
            price = each
    final_dict[details_list[0]] = each

print(final_dict)   
# s = all_products[0].text.split()
# print(type(s))

driver.close()