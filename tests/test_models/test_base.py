#!/usr/bin/python3
"""Unit test for BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit test for BaseModel class"""

    """
    @classmethod
    def SetUp(cls):
        print('SetupClass')

    @classmethod
    def TearDown(cls):
        print('TearDownClass')

    def setup(self):
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def teardown(self):
        del self.bm1
        del self.bm2
    """
    def test_uuid(self):
        """Test for uuid"""
        print("testing uuid...")
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_str(self):
        """Test for __str__ method"""
        print("testing __str__method...")
        pass

    def test_save(self):
        """Test for save method"""
        print("testing save method...")
        pass

    def test_module_docstring(self):
        """Test for existence of module docstring"""
        print("testing module docstring...")
        pass

    def test_created_at(self):
        """Test for created at time"""
        print("Testing the created at time attr")
        pass

    def test_updated_at(self):
        """Test for the updated at time attr"""
        print("Testing the updated at time attr")
        bm1 = BaseModel()
        prechange = bm1.updated_at
        bm1.save()
        postchange = bm1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_kwargs(self):
        """Test for kwargs"""
        print("Testing for kwargs")
        bm1 = BaseModel()
        bm1.name = "Holberton"
        bm1.my_number = 89
        bm1_json = bm1.to_dict()

        bm2 = BaseModel(**bm1_json)
        self.assertEqual(bm1.id, bm2.id)
        self.assertEqual(bm1.created_at, bm2.created_at)
        self.assertEqual(bm1.updated_at, bm2.updated_at)
        self.assertEqual(bm1.name, bm2.name)
        self.assertEqual(bm1.my_number, bm2.my_number)

    if __name__ == "__main__":
        unittest.main()
