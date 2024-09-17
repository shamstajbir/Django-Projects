from django.test import TestCase
from .models import Contact

class ContactModelTests(TestCase):
    def setUp(self):
        Contact.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            address="123 Elm Street"
        )

    def test_contact_creation(self):
        contact = Contact.objects.get(email="john.doe@example.com")
        self.assertEqual(contact.first_name, "John")
        self.assertEqual(contact.last_name, "Doe")
        self.assertEqual(contact.phone_number, "1234567890")
        self.assertEqual(contact.address, "123 Elm Street")

    def test_contact_str_method(self):
        contact = Contact.objects.get(email="john.doe@example.com")
        self.assertEqual(str(contact), "John Doe")
