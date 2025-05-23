from django.test import TestCase
from .models import Category, Image
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Landscape")
        self.assertEqual(category.name, "Landscape")
        self.assertIsInstance(category, Category)
        self.assertEqual(str(category), "Landscape")

class ImageModelTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Portrait")
        self.category2 = Category.objects.create(name="Abstract")

    def test_create_image_with_categories(self):
        test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x89\x61',
            content_type='image/jpeg'
        )
        image = Image.objects.create(
            title="My Masterpiece",
            image=test_image,
            created_date=timezone.now().date(),
            age_limit=12
        )
        image.categories.set([self.category1, self.category2])

        self.assertEqual(image.title, "My Masterpiece")
        self.assertEqual(image.age_limit, 12)
        self.assertEqual(image.categories.count(), 2)
        self.assertIn(self.category1, image.categories.all())
        self.assertIn(self.category2, image.categories.all())
        self.assertIsInstance(image, Image)
