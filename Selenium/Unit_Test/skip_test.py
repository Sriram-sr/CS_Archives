import unittest

class Test_class(unittest.TestCase):
    def test_method_1(self):
        print('This is the first test case')
    @unittest.skip('Skipped because it is not ready')   #This is used for skipping with a message    
    def test_method_2(self):
        print('This is the second test case') 
    @unittest.SkipTest    #This decorater is used for skipping this particular test method
    def test_method_3(self):
        print('This is the third test case') 
    unittest.skipIf(1==1,'You have to specify a condition as a first arg to skip this test')    
    def test_method_4(self):
        print('This is fourth test case')  

if __name__ == '__main__' :
    unittest.main()           