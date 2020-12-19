import unittest
from main import Calculate


class TestAOCDay18(unittest.TestCase):
    def testSmallStringAdd(self):
        calc_result = Calculate("3 + 3")

        self.assertEqual(calc_result, 6)

    def testSmallStringMultiply(self):
        calc_result = Calculate("3 * 3")

        self.assertEqual(calc_result, 9)

    def testReturnNumber(self):
        calc_result = Calculate("465")

        self.assertEqual(calc_result, 465)

    def testLongString(self):
        calc_result = Calculate("3 + 3 * 2")

        self.assertEqual(calc_result, 12)
