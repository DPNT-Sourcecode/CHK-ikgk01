import unittest
from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout(unittest.TestCase):
    # Happy path testing
    def test_add(self):
        self.assertEqual(CheckoutSolution().checkout("r"), -1, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("aaabb"), -1, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("AAAABBB"), 255, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("ABCD"), 115, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("AAABB"), 175, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("R"), -1, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("AAABBbCCDD"), -1, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("AAAAABBBEE"), 325, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("AAAAABBBEEEE"), 390, "Not correct!")

        


