from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from khanto.models import Announcement, Property


class AnnouncementModelTestCase(TestCase):
    """Class to test announcement model."""
    fixtures = ['properties_fixtures', 'announcements_fixtures']

    def setUp(self):
        """."""
        self.announcement = Announcement.objects.first()
        self.property = Property

    def test_announcement_model_fields(self):
        """Enrure that fields receive correct types."""
        self.assertIsInstance(self.announcement.property, Property)
        self.assertIsInstance(self.announcement.plataform_name, str)
        self.assertIsInstance(self.announcement.plataform_rate, float)
        self.assertIsInstance(self.announcement.created_at, date)
        self.assertIsInstance(self.announcement.updated_at, date)

    def test_minimum_announcement_plataform_rate_exception(self):
        """Ensure that value of plataform rate is greather than 0."""
        with self.assertRaises(ValidationError):
            self.announcement.plataform_rate = -1
            self.announcement.full_clean()
            self.announcement.save()
