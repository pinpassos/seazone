from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from khanto.models import Property


class PropertyModelTestCase(TestCase):
    """Class to test property model."""
    fixtures = ['properties_fixtures']

    def setUp(self):
        """."""
        self.property = Property.objects.first()

    def test_property_model_fields(self):
        """Enrure that fields receive correct types."""
        self.assertIsInstance(self.property.code, str)
        self.assertIsInstance(self.property.number_of_guests, int)
        self.assertIsInstance(self.property.number_of_bathrooms, int)
        self.assertIsInstance(self.property.allowed_pet, bool)
        self.assertIsInstance(self.property.cleaning_cost, float)
        self.assertIsInstance(self.property.activation_date, date)
        self.assertIsInstance(self.property.created_at, date)
        self.assertIsInstance(self.property.updated_at, date)

    def test_minimum_guests_in_property_exception(self):
        """Ensure that number of guests is greather than 0."""
        with self.assertRaises(ValidationError):
            self.property.number_of_guests = 0
            self.property.full_clean()

    def test_minimum_cleaning_cost_exception(self):
        """Ensure that price of cleaning cost is greather than 0.0"""
        with self.assertRaises(ValidationError):
            self.property.cleaning_cost = -1
            self.property.full_clean()
