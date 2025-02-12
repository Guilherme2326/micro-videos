import unittest
from datetime import datetime
from src.category.domain.entities import Category

class TestCategory(unittest.TestCase):
    def teste_constructor(self):
       category = Category('Movie', 'some description', True, datetime.now())
       self.assertEqual(category.name, 'Movie')   
       self.assertEqual(category.description, 'some description')
       self.assertTrue(category.is_active)
       self.assertIsInstance(category.created_at, datetime)