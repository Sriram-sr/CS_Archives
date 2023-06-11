import unittest

# import all classes which are distinct test cases

from Sanity import LoginTest,SignUpTest
from Functional import Cash_Deposit,Cash_Withdrawal

# creating objects for all test cases

test_case_1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
test_case_2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
test_case_3 = unittest.TestLoader().loadTestsFromTestCase(Cash_Deposit)
test_case_4 = unittest.TestLoader().loadTestsFromTestCase(Cash_Withdrawal)

# Creating a test suite for sanity test which contains different test cases like login,signup

Sanity_TestSuite = unittest.TestSuite([test_case_1,test_case_2])
Functional_Testsuite = unittest.TestSuite([test_case_3,test_case_4])

# unittest.TextTestRunner().run(Sanity_TestSuite)
# unittest.TextTestRunner().run(Functional_Testsuite)



