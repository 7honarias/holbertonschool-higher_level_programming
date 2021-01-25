import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_width(self):
        r = Rectangle(2, 3)
        self.assertAlmostEqual(r.width, 2)
        self.assertAlmostEqual(r.height, 3)
        self.assertAlmostEqual(type(r), Rectangle)
        self.assertAlmostEqual(r.area(), 6)

    def test_rectangle_init(self):
        r1 = Rectangle(2, 3)
        self.assertAlmostEqual(r1.id, 2)
        b2 = Rectangle(2, 4)
        self.assertAlmostEqual(b2.id, 3)

    def test_raise(self):
        r3 = Rectangle(2, 3)
        assertIsInstance(r3, Rectangle, msg=None)


    def tearDown(self):
        Base._Base__nb_objects = 0

