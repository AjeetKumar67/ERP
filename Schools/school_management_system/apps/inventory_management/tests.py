from django.test import TestCase
from .models import Supply, Uniform

class InventoryManagementTests(TestCase):

    def setUp(self):
        self.supply = Supply.objects.create(name="Pencils", quantity=100, price=0.50)
        self.uniform = Uniform.objects.create(name="School T-Shirt", size="M", price=10.00)

    def test_supply_creation(self):
        self.assertEqual(self.supply.name, "Pencils")
        self.assertEqual(self.supply.quantity, 100)
        self.assertEqual(self.supply.price, 0.50)

    def test_uniform_creation(self):
        self.assertEqual(self.uniform.name, "School T-Shirt")
        self.assertEqual(self.uniform.size, "M")
        self.assertEqual(self.uniform.price, 10.00)

    def test_supply_str(self):
        self.assertEqual(str(self.supply), "Pencils")

    def test_uniform_str(self):
        self.assertEqual(str(self.uniform), "School T-Shirt")