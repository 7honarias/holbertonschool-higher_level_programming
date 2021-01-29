#!/usr/bin/python3
""" This is a Unittest module """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """ Test Cases for Base Class """

    def setUp(self):
        """This method set up initial state for all test methods"""
        Base._Base__nb_objects = 0
        # print("setUp")

    def test_id_single(self):
        """ Test for set id function """
        b0 = Base(1)
        self.assertEqual(b0.id, 1)

    def test_id_none(self):
        """ Test for set id function """
        b0 = Base(None)
        self.assertEqual(b0.id, 1)

    def test_id_multiple(self):
        """ Test for set id function """
        b0 = Base()
        b1 = Base()
        self.assertEqual(b0.id, 1)
        self.assertEqual(b1.id, 2)

    def test_id_error(self):
        """ Test for set id function """
        self.assertEqual("Juan", Base("Juan").id)
        self.assertEqual(2.5, Base(2.5).id)
        self.assertEqual([1, 2], Base([1, 2]).id)
        self.assertEqual({'1': 2}, Base({'1': 2}).id)
        self.assertEqual(True, Base(True).id)

    def test_rectangle_save_to_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            result = file.read()
            self.assertEqual(result, '[]')

        # check for square object
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lambda x: ord(x), '[{"y": 2, "x": 7, '
                                        '"id": 8, "size": 10}, '
                                        '{"y": 0, "x": 4, "id": 1, '
                                        '"size": 2}]')))
            self.assertEqual(sum_read, sum_expected)

    ef test_load_from_file(self):
        """Checks for load_from_file
        """
        # Check for rectangle load from file
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output), "[]")

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def tearDown(self):
        """Tear down test method to reset class attribute
        """
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass
        try:
            os.remove("Rectangle.csv")
        except Exception:
            pass
        try:
            os.remove("Square.csv")
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()