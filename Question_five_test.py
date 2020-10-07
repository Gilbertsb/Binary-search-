import unittest
import Question_five


class MyTestCase(unittest.TestCase):
    def test_binnary(self):
        test=Question_five.binary_search([1,2,3,4,5,6,7],4)
        self.assertTrue(test,True)
    def test_binnary2(self):
        test=Question_five.binary_search([1,2,3,4,5,6,7],12)
        self.assertFalse(test,False)
    def test_binnary3(self):
        test=Question_five.binary_search([],1)
        self.assertFalse(test,False)

if __name__ == '__main__':
    unittest.main()
