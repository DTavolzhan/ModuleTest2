from django.test import TestCase
from .models import Category, Image

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Landscape")
        self.assertEqual(category.name, "Landscape")
        self.assertIsInstance(category, Category)
        self.assertEqual(str(category), "Landscape")

