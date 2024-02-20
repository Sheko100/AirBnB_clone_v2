#!/usr/bin/python3
"""Unittest for the console commands
"""

from console import HBNBCommand
import os
import unittest


class TestConsole(unittest.TestCase):
    """Tests for the console commands
    """

    def test_create_with_string_params(self):
        """Test that the create command accepts parameters as strings data for
        the created object
        """
        arg_str = 'State name="Kafr_El-Shaikh"'
        new_cmd = HBNBCommand()
        objects = new_cmd.objects
        state_exists = False

        start_count = len(objects)
        new_cmd.do_create(arg_str)

        for dct in objects.values():
            if hasattr(dct, 'name') and dct.name == 'Kafr El-Shaikh':
                state_exists = True
                break

        end_count = len(objects)
        self.assertTrue(state_exists and end_count - start_count == 1)

    def test_create_with_integer_params(self):
        """Test that the create command accepts parameters as Integers data for
        the created object
        """
        arg_str = """Place city_id="0001" user_id="0001" name="My_little_house"
        number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300"""
        new_cmd = HBNBCommand()
        objects = new_cmd.objects
        object_exists = False

        start_count = len(objects)
        new_cmd.do_create(arg_str)

        for dct in objects.values():
            if hasattr(dct, 'max_guest') and dct.max_guest == 10:
                object_exists = True
                break

        end_count = len(objects)
        self.assertTrue(object_exists and end_count - start_count == 1)

    def test_create_with_positive_float_params(self):
        """Test that the create command accepts parameters as positive
        floats data for the created object
        """
        arg_str = """Place city_id="0002" user_id="0002" name="Test"
        number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300
        latitude=37.773972 longitude=-122.431297"""
        new_cmd = HBNBCommand()
        objects = new_cmd.objects
        object_exists = False

        start_count = len(objects)
        new_cmd.do_create(arg_str)

        for dct in objects.values():
            if hasattr(dct, 'latitude') and dct.latitude == 37.773972:
                object_exists = True
                break

        end_count = len(objects)
        self.assertTrue(object_exists and end_count - start_count == 1)

    def test_create_with_negative_float_params(self):
        """Test that the create command accepts parameters as negative
        floats data for the created object
        """
        arg_str = """Place city_id="0002" user_id="0002" name="Test"
        number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300
        latitude=37.773972 longitude=-122.431297"""
        new_cmd = HBNBCommand()
        objects = new_cmd.objects
        object_exists = False

        start_count = len(objects)
        new_cmd.do_create(arg_str)

        for dct in objects.values():
            if hasattr(dct, 'longitude') and dct.longitude == -122.431297:
                object_exists = True
                break

        end_count = len(objects)
        self.assertTrue(object_exists and end_count - start_count == 1)
