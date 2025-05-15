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
        self.assertEqual(CheckoutSolution().checkout("AAABBbCCDD"), -1, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("AAAAABBBEE"), 325, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("AAAAABBBEEFF"), 345, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("AAAAABBBEEFFF"), 345, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("AAAAABBBEEFFFF"), 355, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("G"), 20, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("HHHH"), 40, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("HHHHH"), 45, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("HHHHHH"), 55, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("HHHHHHHHHH"), 80, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("I"), 35, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("J"), 60, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("K"), 80, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("KK"), 150, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("L"), 90, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("M"), 15, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("N"), 40, "Not correct!")
        self.assertEqual(CheckoutSolution().checkout("NNNM"), 120, "Not correct!")

        


