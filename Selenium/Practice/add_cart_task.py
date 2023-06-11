from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path = "C:\\Linux_Backup\\Selenium\\chromedriver.exe")
driver.maximize_window()

driver.get('http://demostore.supersqa.com/')
driver.implicitly_wait(5)
product = driver.find_element_by_css_selector('#main > ul > li.product.type-product.post-16.status-publish.instock.product_cat-accessories.has-post-thumbnail.sale.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
  # Finding a cloth named 'Beanie' and clicking add to cart button using its copy selector function
product.click()   # clicking that element

cart_page = driver.find_element_by_xpath('//*[@id="site-navigation"]/div[1]/ul/li[2]/a')
cart_page.click()

driver.refresh()

# Sending a fake coupon code and retreiving the alert message returned

coupon_box = driver.find_element_by_name('coupon_code')
coupon_box.send_keys('fakeone')
apply_box = driver.find_element_by_name('apply_coupon')
apply_box.click()

sleep(3)

alert_text = driver.find_element_by_xpath('//*[@id="post-7"]/div/div/div[1]/ul/li')
print(f'\nThe exception is :{alert_text.text}')