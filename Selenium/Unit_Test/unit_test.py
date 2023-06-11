import unittest
from selenium import webdriver
from time import sleep

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')
        self.driver.get('http://www.google.com/')
        print(self.driver.title)
        sleep(3)
        self.driver.close()
    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')
        self.driver.get('http://bing.com')
        print(self.driver.title)
        sleep(3)

if __name__ == '__main__':
    unittest.main()        