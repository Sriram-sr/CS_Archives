import unittest
from selenium import webdriver

class TestingClass(unittest.TestCase):
    def test_webpage_title(self):
        driver = webdriver.Chrome(executable_path = '/home/sriram/Selenium/chromedriver')
        driver.get('http://www.google.com')
        page_title = driver.title
        # self.assertEqual("Google",page_title,'Failed because titles are not matched')
        # This assertEqual method is used when expected output is matched with the current output from the page\
        # or else the reason given in the third argument will be returned

        # self.assertNotEqual('Googlemap',page_title)  #Test will be passed if the assertion is not equal

        # self.assertTrue(page_title == 'Google')  #if condition inside parentheses becomes true,test is passed

        # self.assertFalse(1==10)  #test is passed if the condition is false
        
        # self.assertIsNone(value)   #if value is none test is passed
        # self.assertIsNotNone(value)  #test is passed is value is not none
        
        assert_list = ['Google','Facebook','Twitter']

        # self.assertIn(page_title,assert_list)  #Test is passed if first element is in \
        # second arg which is any python data structure

        self.assertNotIn('Facebook',assert_list)

if __name__ == '__main__' :
    unittest.main()       