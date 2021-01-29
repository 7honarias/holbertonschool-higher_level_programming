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

    def test_id_single(self):
        """ Test for set id function """
        with self.assertRaises(TypeError):
            b0 = Square()

    def test_id_none(self):
        """ Test for set id function """
        with self.assertRaises(TypeError):
            c1 = Square("1")
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
        with self.assertRaises(TypeError):
            Square.save_to_file([])

    def test_id_multiple(self):
        """ Test for set id function """
        s1 = Square(3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 3)
        s2 = Square(1, 2)
        self.assertEqual(s2.size, 1)
        s3 = Square(1, 2, 3)
        self.assertEqual(s3.x, 2)
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.y, 3)
        my_list = Square.load_from_file()
        Square.save_to_file(None)
        Square.save_to_file([Square(1)])

    def test_str(self):
        """test str"""
        r1 = Square(4, 6, 7, 4)
        self.assertEqual(str(r1), "[Square] (4) 6/7 - 4")
        r2 = Square.create(**{ 'id': 25, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(r2.id, 25)
        r2.update(**{ 'id': 3, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(r2.id, 3)

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