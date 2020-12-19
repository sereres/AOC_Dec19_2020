import unittest
from main import Calculate

class TestAOCDay18(unittest.TestCase):
    def testSmallStringAdd(self):
        calc_result = Calculate("3 + 3")

        self.assertEqual(calc_result, 6)

    def testSmallStringMultiply(self):
        calc_result = Calculate("3 * 3")

        self.assertEqual(calc_result, 9)