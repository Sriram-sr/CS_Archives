import unittest

class AppTesting(unittest.TestCase):
    def test_web(self):
        print('web test done successfully')
    def test_Browser(self):  #All methods should have the prefix 'test'
        print('Browser test done succeessfully')
    @classmethod    
    def setUp(self):
        print('This is login test') #This will be executed before every test method 
    @classmethod
    def tearDown(self):    
        print('This is logout')    #This will executed after every test method 
    @classmethod
    def setUpClass(cls):                
        print('Application Opened')   #This will be  Executed at the start of the class only  one time
    @classmethod
    def tearDownClass(cls):
        print('Application Closed') #This will be executed at the completion of all test cases
        
if __name__ == '__main__' :
    unittest.main()       