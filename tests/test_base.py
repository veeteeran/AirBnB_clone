#!/usr/bin/python3
"""Unit test for BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit test for BaseModel class"""

    def test_uuid(self)
        """Test for uuid"""
        print("testing uuid...")
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    # Add tests for created_at and updated_at???

    def test_str(self)
        """Test for __str__ method"""
        print("testing __str__method...")
        pass

    def test_save(self)
        """Test for save method"""
        print("testing save method...")
        pass

    def test_module_docstring(self):
        """Test for existence of module docstring"""
        print("testing module docstring...")
        pass
