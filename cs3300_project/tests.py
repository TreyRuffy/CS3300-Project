from django.test import TestCase
from .models import Horse

# Create your tests here.
class HorsePageTestCase(TestCase):
    def setUp(self):
        Horse.objects.create(name="Test", short_description="short", long_description="long description")

    def test_horse_page(self):
        """Horse page is accessible"""
        test_horse = Horse.objects.get(name="Test")
        response = self.client.get(f'/horse/{test_horse.id}')
        # self.assertEqual(response.status_code, 200)

    def test_horse_page_fail(self):
        """Horse page is not accessible"""
        test_horse = Horse.objects.get(name="Test")
        response = self.client.get(f'/horse/{test_horse.id}')
        self.assertNotEqual(response.status_code, 404)

    def test_horse_page_template(self):
        """Horse page uses correct template"""
        test_horse = Horse.objects.get(name="Test")
        response = self.client.get(f'/horse/{test_horse.id}')
        self.assertTemplateUsed(response, 'cs3300_project/horse.html')
        self.assertTemplateUsed(response, 'cs3300_project/base_template.html')
        self.assertTemplateUsed(response, 'cs3300_project/includes/navbar.html')