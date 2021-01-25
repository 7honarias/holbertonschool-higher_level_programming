import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_values(self):
        r2 = Base()
        self.assertEqual(r2.id, 1)
        r3 = Base()
        self.assertEqual(r3.id, 2)
        r4 = Base(12)
        self.assertEqual(r4.id, 12)

