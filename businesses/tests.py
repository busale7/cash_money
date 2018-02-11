from django.test import TestCase
from .models import Business

class BusinessModelTestCase(TestCase):
    def test_create(self):
        Business.objects.create(
            name="Coded",
            description="The first coding bootcamp in the middle east",
            established="2015-7-26"
            )