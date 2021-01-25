import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_values(self):
        r2 = Base(2,2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 2)
