from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import pyautogui
from time import sleep
# driver = webdriver.Chrome(executable_path='C:\\Linux_Backup\\Selenium\\chromedriver.exe')
driver = webdriver.Chrome()  # Deprication warning eliminated
driver.maximize_window()
driver.get('https://www.ilovepdf.com/compress_pdf')
driver.implicitly_wait(10)
photo = driver.find_element(By.ID,'pickfiles')
photo.click()
sleep(3) 
pyautogui.click(113,405)
pyautogui.click(358,375)
pyautogui.click(695,665)
# pyautogui.typewrite(r"C:\Linux_Backup\Documents\vi_cheat_sheet.pdf")
# pyautogui.press(['tab','tab','enter'])

# C:\Users\Admin\AppData\Local\Programs\Python\Python310\Scripts  Default python path in windows