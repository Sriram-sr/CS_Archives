import unittest

class LoginTest(unittest.TestCase):
    def test_login_Email(self):
        print('Email login successful')
        self.assertTrue(True)

    def test_login_Facebook(self):
        print('Facebok login successful')
        self.assertTrue(True)

class SignUpTest(unittest.TestCase):
    def test_signup_Email(self):
        print('Email signup successful')
        self.assertTrue(True)

    def test_signupFacebook(self):
        print('Facebook signup successful')
        self.assertTrue(True)

if __name__ == '__main__' :
    unittest.main()                  