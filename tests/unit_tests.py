import unittest
from cashpro.reduction import *

class calculerReductionUnitTest(unittest.TestCase):
  def test_exemple(self):
    self.assertEqual(calculerReduction(50, False), 0)
    self.assertEqual(calculerReduction(200, False), 0)
    self.assertEqual(calculerReduction(15, True), 0)
    self.assertEqual(calculerReduction(32, True), 0)
    self.assertEqual(calculerReduction(100, True), 0)
    self.assertEqual(calculerReduction(201, True), 0)
if __name__ == '__main__':
  unittest.main()
