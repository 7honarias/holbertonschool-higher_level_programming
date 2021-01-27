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
        # print("tearDown")

    def test_id_single(self):
        """ Test for set id function """
        with self.assertRaises(TypeError):
            b0 = Square()

    def test_id_none(self):
        """ Test for set id function """
        pass

    def test_id_multiple(self):
        """ Test for set id function """
        s1 = Square(3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 3)
