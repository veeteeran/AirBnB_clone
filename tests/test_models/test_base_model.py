#!/usr/bin/python3
"""Unit test for BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit test for BaseModel class"""

    @classmethod
    def setUp(cls):
        print('SetupClass')

    @classmethod
    def tearDown(cls):
        print('TearDownClass')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def tearDown(self):
        """Unit test tear down"""
        del self.bm1
        del self.bm2

    def test_uuid(self):
        """Test for uuid"""
        print("testing uuid...")
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertNotEqual(self.bm1.id, self.bm2.id)
        self.assertIsInstance(self.bm1.id, str)

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
        prechange = self.bm1.updated_at
        self.bm1.save()
        postchange = self.bm1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_kwargs(self):
        """Test for kwargs"""
        print("Testing for kwargs")
        self.bm1.name = "Holberton"
        self.bm1.my_number = 89
        bm1_json = self.bm1.to_dict()

        bm2 = BaseModel(**bm1_json)
        self.assertEqual(self.bm1.id, bm2.id)
        self.assertEqual(self.bm1.created_at, bm2.created_at)
        self.assertEqual(self.bm1.updated_at, bm2.updated_at)
        self.assertEqual(self.bm1.name, bm2.name)
        self.assertEqual(self.bm1.my_number, bm2.my_number)

    if __name__ == "__main__":
        unittest.main()
