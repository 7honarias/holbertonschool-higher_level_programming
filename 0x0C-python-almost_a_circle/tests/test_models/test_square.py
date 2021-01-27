#!/usr/bin/python3
""" This is a Unittest module """


import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """ Test Cases for Base Class """

    def setUp(self):
        """This method set up initial state for all test methods"""
        Base._Base__nb_objects = 0
        # print("setUp")

    def tearDown(self):
        """This method to perform cleanup after each test method completes"""
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

    def test_id_single(self):
        """ Test for set id function """
        with self.assertRaises(TypeError):
            b0 = Square()

    def test_id_none(self):
        """ Test for set id function """
        with self.assertRaises(TypeError):
            b0 = Square(None)
        with self.assertRaises(TypeError):
            r2 = Square(1, "2")
        with self.assertRaises(TypeError):
            r3 = Square(1, 2, "3")
        with self.assertRaises(ValueError):
            r5 = Square(-1, 2)
        with self.assertRaises(ValueError):
            r6 = Square(1, -2)
        with self.assertRaises(ValueError):
            r7 = Square(0, 1)
        with self.assertRaises(ValueError):
            r9 = Square(1, 2, -3)

    def test_id_multiple(self):
        """ Test for set id function """
        s1 = Square(3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 3)

    def test_str(self):
        """test str"""
        r1 = Square(4, 6, 7, 4)
        self.assertEqual(str(r1), "[Square] (4) 6/7 - 4")

 