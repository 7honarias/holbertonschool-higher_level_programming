#!/usr/bin/python3
""" This is a Unittest module """

import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    """ Test Cases for Base Class """

    def setUp(self):
        """This method set up initial state for all test methods"""
        Base._Base__nb_objects = 0
        # print("setUp")

    def tearDown(self):
        """This method to perform cleanup after each test method completes"""
        # print("tearDown")

    def test_id_single(self):
        """ Test for set id function """
        rect = Rectangle(3, 2)
        area = rect.area()
        self.assertEqual(area, 6)

        r2 = Rectangle(10, 2, 1, 9, 30)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(r2_dictionary, {'x': 1, 'y': 9, 'id': 30, 'height': 2,
                                         'width': 10})

        output_4 = "  ##\n  ##\n"
        r4 = Rectangle(2, 2, 2, 0)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r4.display()
            self.assertEqual(mock_out.getvalue(), output_4)

        output_5 = "\n\n  ##\n  ##\n"
        r5 = Rectangle(2, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r5.display()
            self.assertEqual(mock_out.getvalue(), output_5)

        output_1 = "#\n"
        r1 = Rectangle(1, 1)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            r1.display()
            self.assertEqual(mock_out.getvalue(), output_1)

    def test_id_none(self):
        """ Test for set id function """
        with self.assertRaises(TypeError):
            b0 = Rectangle()
        with self.assertRaises(TypeError):
            b0 = Rectangle(None)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            b1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            r5 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r6 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r7 = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r8 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r9 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r10 = Rectangle(1, 2, 3, -4)
        with self.assertRaises(TypeError):
            r11 = Rectangle(10, 4, 5, 10, 30, 60)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([])
        with self.assertRaises(AttributeError):
            r2 = None
            r2.to_dictionary
        
    def test_id_error(self):
        """ Test for set id function """
        r = Rectangle(1,2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.display(), None)

        r5 = Rectangle(10, 2, 4, 5, 50)
        self.assertEqual(r5.id, 50)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 4)
        self.assertEqual(r5.y, 5)
        rect2 = Rectangle(10, 2, 1, 9, 30)
        rect2_dictionary = rect2.to_dictionary()
        self.assertEqual(rect2_dictionary, {'x': 1, 'y': 9, 'id': 30, 'height': 2,
                                         'width': 10})
        Rectangle.save_to_file(None)
        
        Rectangle.save_to_file([Rectangle(1, 2)])
        rect4 = Rectangle(1, 1)
        my_list = rect4.load_from_file()
                                        
    def test_str(self):
        """test str"""
        r1 = Rectangle(4, 6, 7, 4, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 7/4 - 4/6")

    def test_update(self):
        """Checks update method
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        r2 = Rectangle.create(**{ 'id': 89, 'width': 4, 'height': 2 })
        self.assertEqual(r2.width, 4)
        r3 = Rectangle.create(**{ 'id': 8, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(r3.id, 8)
        r4 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(r4.x, 3)
        Rectangle.save_to_file(None)