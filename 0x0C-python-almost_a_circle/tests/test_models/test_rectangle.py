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

    def test_id_error(self):
        """ Test for set id function """
        r = Rectangle(1,2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

