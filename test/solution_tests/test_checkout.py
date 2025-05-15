import unittest
from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout(unittest.TestCase):
    # Happy path testing
    def test_add(self):
        self.assertEqual(CheckoutSolution().checkout("r"), -1, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("r"), -1, "Not correct!")
        #self.assertEqual(Calculator.add(-6, 4), -2, "Not correct!")
        #self.assertEqual(Calculator.add(6, -4), 2, "Not correct!")
        #self.assertEqual(Calculator.add(-6, -4), -10, "Not correct!")