#!/usr/bin/python3
"""Unit test for Place class"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestBaseModel(unittest.TestCase):
    """Unit test for Place class"""

    @classmethod
    def setUp(cls):
        print('SetupClass')

    @classmethod
    def tearDown(cls):
        print('TearDownClass')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.p1 = Place()
        self.p2 = Place()

    def tearDown(self):
        """Unit test tear down"""
        del self.p1
        del self.p2

    def test_init(self):
        """Test for init method"""
        print("testing init...")
        self.assertIsNotNone(self.p1)
        self.assertIsInstance(self.p1, BaseModel)
        self.assertIs(type(self.p1), Place)

    def test_city_id(self):
        """Test for city_id attribute"""
        print("testing city_id...")
        self.assertTrue(hasattr(self.p1, "city_id"))
        self.assertEqual(self.p1.city_id, "")
        self.assertIsInstance(self.p1.city_id, str)

    def test_user_id(self):
        """Test for user_id attribute"""
        print("testing user_id...")
        self.assertTrue(hasattr(self.p1, "user_id"))
        self.assertEqual(self.p1.user_id, "")
        self.assertIsInstance(self.p1.user_id, str)

    def test_name(self):
        """Test for name attribute"""
        print("testing name...")
        self.assertTrue(hasattr(self.p1, "name"))
        self.assertEqual(self.p1.name, "")
        self.assertIsInstance(self.p1.name, str)

    def test_description(self):
        """Test for description attribute"""
        print("testing description...")
        self.assertTrue(hasattr(self.p1, "description"))
        self.assertEqual(self.p1.description, "")
        self.assertIsInstance(self.p1.description, str)

    def test_number_rooms(self):
        """Test for number_rooms attribute"""
        print("testing number_rooms...")
        self.assertTrue(hasattr(self.p1, "number_rooms"))
        self.assertEqual(self.p1.number_rooms, 0)
        self.assertIsInstance(self.p1.number_rooms, int)

    def test_number_bathrooms(self):
        """Test for number_bathrooms attribute"""
        print("testing number_bathrooms...")
        self.assertTrue(hasattr(self.p1, "number_bathrooms"))
        self.assertEqual(self.p1.number_bathrooms, 0)
        self.assertIsInstance(self.p1.number_bathrooms, int)

    def test_max_guest(self):
        """Test for max_guest attribute"""
        print("testing max_guest...")
        self.assertTrue(hasattr(self.p1, "max_guest"))
        self.assertEqual(self.p1.max_guest, 0)
        self.assertIsInstance(self.p1.max_guest, int)

    def test_price_by_night(self):
        """Test for price_by_night attribute"""
        print("testing price_by_night...")
        self.assertTrue(hasattr(self.p1, "price_by_night"))
        self.assertEqual(self.p1.price_by_night, 0)
        self.assertIsInstance(self.p1.price_by_night, int)

    def test_latitude(self):
        """Test for latitude attribute"""
        print("testing latitude...")
        self.assertTrue(hasattr(self.p1, "latitude"))
        self.assertEqual(self.p1.latitude, 0.0)
        self.assertIsInstance(self.p1.latitude, float)

    def test_longitude(self):
        """Test for longitude attribute"""
        print("testing longitude...")
        self.assertTrue(hasattr(self.p1, "longitude"))
        self.assertEqual(self.p1.longitude, 0.0)
        self.assertIsInstance(self.p1.longitude, float)

    def test_amenity_ids(self):
        """Test for amenity_ids attribute"""
        print("testing amenity_ids...")
        self.assertTrue(hasattr(self.p1, "amenity_ids"))
        self.assertEqual(self.p1.amenity_ids, "")
        self.assertIsInstance(self.p1.amenity_ids, str)

    if __name__ == "__main__":
        unittest.main()
