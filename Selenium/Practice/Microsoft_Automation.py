from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')
    driver.maximize_window()

    driver.get('https://www.office.com/')

    sign_in = driver.find_element(By.ID,'hero-banner-sign-in-to-office-365-link')
    sign_in.click()
    # sleep(5)

    login_id = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,'loginfmt')))
    login_id.send_keys('cloudbrinktest1@outlook.com')

    nxt_btn = driver.find_element(By.ID,'idSIButton9')
    nxt_btn.click()

    passwd = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,'passwd')))
    passwd.send_keys('Automationtest@123')

    sign_in = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'idSIButton9')))
    sign_in.click()

    Dont_show_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'KmsiCheckboxField')))
    Dont_show_btn.click()

    yes_btn = driver.find_element(By.ID,'idSIButton9')
    yes_btn.click()
    sleep(5)
    one_drive = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ShellDocuments_link"]/div/i')))
    one_drive.click()
    # sleep(5)

    upload_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Upload']")))
    print(upload_btn)
    upload_btn.click()
except Exception as e:
    print(e)