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
    
    def test_from_json_string(self):
        """Checks from_json_string method
        """
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89},
                                       {'height': 7, 'width': 1, 'id': 7}])
        self.assertTrue(type(list_output) == list)

        list_input = [
                    {'id': 89, 'width': 10, 'height': 4, 'x': 3, 'y': 2},
                    {'id': 7, 'width': 1, 'height': 7, 'x': 3}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89,
                                        'x': 3, 'y': 2},
                                       {'height': 7, 'width': 1, 'id': 7,
                                        'x': 3}])
        self.assertTrue(type(list_output) == list)

        list_input = [
                    {'id': 89, 'width': 10, 'height': 4, 'x': 3, 'y': 2},
                    {'id': 7, 'width': 1, 'height': 7, 'x': 3}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89,
                                        'x': 3, 'y': 2},
                                       {'height': 7, 'width': 1,
                                        'id': 7, 'x': 3}])
        self.assertTrue(type(list_output) == list)

        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertTrue(type(list_output) == list)

        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertTrue(type(list_output) == list)

    def test_save_to_file(self):
        """Checks save_to_file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lambda x: ord(x), '[{"y": 8, "x": 2, '
                                        '"id": 1, "width": 10, "height": 7}, '
                                        '{"y": 0, "x": 0, "id": 2, '
                                        '"width": 2, "height": 4}]')))
            self.assertEqual(sum_read, sum_expected)

        r1 = Rectangle(10, 7)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lambda x: ord(x), '[{"y": 0, "x": 0, '
                                        '"id": 3, "width": 10, "height": 7}, '
                                        '{"y": 0, "x": 0, "id": 4, '
                                        '"width": 2, "height": 4}]')))
            self.assertEqual(sum_read, sum_expected)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

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

    def test_load_from_file(self):
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
        list_square_output = Square.load_from_file()
        self.assertEqual(str(list_square_output), "[]")

        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

        s1 = Square(10, 50)
        s2 = Square(2, 0, 0, 89)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

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