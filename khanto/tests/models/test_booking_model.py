from datetime import date
from uuid import UUID

from django.core.exceptions import ValidationError
from django.test import TestCase

from khanto.models import Announcement, Booking


class BookingModelTestCase(TestCase):
    """Class to test booking model."""
    fixtures = ['properties_fixtures',
                'announcements_fixtures', 'bookings_fixtures']

    def setUp(self):
        """."""
        self.booking = Booking.objects.first()
        self.announcement = Announcement

    def test_booking_model_fields(self):
        """Enrure that fields receive correct types."""
        self.assertIsInstance(self.booking.code, UUID)
        self.assertIsInstance(self.booking.announcement, self.announcement)
        self.assertIsInstance(self.booking.check_in, date)
        self.assertIsInstance(self.booking.check_out, date)
        self.assertIsInstance(self.booking.total_price, float)
        self.assertIsInstance(self.booking.number_of_guests, int)
        self.assertIsInstance(self.booking.comment, str)
        self.assertIsInstance(self.booking.created_at, date)
        self.assertIsInstance(self.booking.updated_at, date)

    def test_get_number_of_days(self):
        """test function get number of days."""
        number_of_days = self.booking.get_number_of_days()
        self.assertIsInstance(number_of_days, int)
        self.assertEqual(number_of_days, 4)

    def test_get_total_price_per_guest(self):
        """test function get total price per guest."""
        total_price_per_guest = self.booking.get_total_price_per_guest()
        self.assertIsInstance(total_price_per_guest, float)
        self.assertEqual(total_price_per_guest, 500.0)

    def test_get_total_price_per_guest_multiplied_by_days(self):
        """test function get total price per guest multiplied by days."""
        total_price_per_guest_multiplied_by_days = self.booking.get_total_price_per_guest_multiplied_by_days()
        self.assertIsInstance(total_price_per_guest_multiplied_by_days, float)
        self.assertEqual(total_price_per_guest_multiplied_by_days, 2000.0)

    def test_calculate_total_price_of_booking(self):
        """test function calculate total price of booking."""
        calculate_total_price_of_booking = self.booking.calculate_total_price_of_booking()
        self.assertIsInstance(calculate_total_price_of_booking, float)
        self.assertEqual(calculate_total_price_of_booking, 3980.0)

    def test_ensure_checkin_is_smaller_than_checkout_exception(self):
        """ensure that check_in is smaller than check_out."""
        with self.assertRaises(ValidationError):
            self.booking.check_in = date(2023, 6, 30)
            self.booking.check_out = date(2023, 6, 28)
            self.booking.clean()

    def test_ensure_number_of_guests_smaller_than_property_number_of_guests_exception(self):
        """ensure that number of guests is smaller or equal than property number of guests."""
        with self.assertRaises(ValidationError):
            self.booking.number_of_guests = 3
            self.booking.clean()
