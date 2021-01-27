#!/usr/bin/python3
""" This is a Unittest module """


import unittest
from models.rectangle import Rectangle
from models.base import Base


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
        with self.assertRaises(TypeError):
            b0 = Rectangle()

    def test_id_none(self):
        """ Test for set id function """
        with self.assertRaises(TypeError):
            b0 = Rectangle(None)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, 3, "4")
        r5 = Rectangle(1, 2, 3, 4, 5)

    def test_id_error(self):
        """ Test for set id function """
        r = Rectangle(1,2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.display(), None)

