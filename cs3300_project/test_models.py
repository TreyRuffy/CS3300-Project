from django.test import TestCase
from .models import Horse

class HorseTestCase(TestCase):
    def setUp(self):
        Horse.objects.create(name="Test", short_description="short", long_description="long description")

    def test_horse_name(self):
        """Horse name is correct"""
        test_horse = Horse.objects.get(name="Test")
        self.assertEqual(test_horse.name, "Test")

    def test_horse_name_fail(self):
        """Horse name is incorrect"""
        test_horse = Horse.objects.get(name="Test")
        self.assertNotEqual(test_horse.name, "Test1")

    def test_horse_short_description(self):
        """Horse short description is correct"""
        test_horse = Horse.objects.get(name="Test")
        self.assertEqual(test_horse.short_description, "short")

    def test_horse_short_description_fail(self):
        """Horse short description is incorrect"""
        test_horse = Horse.objects.get(name="Test")
        self.assertNotEqual(test_horse.short_description, test_horse.long_description)
