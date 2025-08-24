from django.test import TestCase
from .models import Products, User

# Create your tests here.
class TestPlumule(TestCase):
    def setUp(self):
        
        self.product1 = Products.objects.create(
            name="Scissors", price=12.04
        )
        self.user = User.objects.create(
            username="Wat", password="123456"
        )
        
    def test_create_product(self):
        
        product = Products.objects.get(name="Scissors")
        self.assertEqual(product.name, "Scissors")
        self.assertEqual(product.price, 12.04)
        self.assertEqual(str(product), "Scissors -> 12.04")