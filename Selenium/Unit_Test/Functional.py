import unittest

class Cash_Deposit(unittest.TestCase):
    def test_using_AccountNumber(self):
        print('Deposit using account number done')
        self.assertTrue(True)

    def test_using_Mobile(self):
        print('Deposit using mobile done')
        self.assertTrue(True)

class Cash_Withdrawal(unittest.TestCase):
    def test_using_AccountNumber(self):
        print('Withdraw using account number done')
        self.assertTrue(True)

    def test_using_Mobile(self):
        print('withdraw using mobile number')
        self.assertTrue(True)

if __name__ == '__main__' :
    unittest.main()                         