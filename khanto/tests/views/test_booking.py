from datetime import date

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status


class BookingViewTestCase(TestCase):
    fixtures = ['properties_fixtures',
                'announcements_fixtures', 'bookings_fixtures']

    def setUp(self):
        """."""
        self.client = Client()
        self.payload = {
            "announcement": {
                "property": {
                    "code": "tst",
                    "number_of_guests": 4,
                    "number_of_bathrooms": 2,
                    "allowed_pet": True,
                    "cleaning_cost": 250,
                    "activation_date": date(2022,6,1)
                },
                "plataform_name": "TESTBNB",
                "plataform_rate": 280
            },
            "check_in": date(2022,7,1),
            "check_out": date(2022,7,6),
            "number_of_guests": 2,
            "comment": "Booking for test"
        }

    def test_booking_view_get_list_response(self):
        """Ensure get list method returns correct data."""
        url_base_name = reverse('bookings-api-list')
        request_get = self.client.get(url_base_name)
        request_json = request_get.json()
        self.assertEqual(request_get.status_code, 200)
        self.assertIsInstance(request_json, list)
        self.assertGreater(len(request_json), 0)

    def test_booking_view_get_detail_response(self):
        """Ensure get detail method returns correct data."""
        url_base_name = reverse('bookings-api-detail', args=[1])
        request_get = self.client.get(url_base_name)
        request_json = request_get.json()
        self.assertEqual(request_get.status_code, 200)
        self.assertIsInstance(request_json, dict)
        self.assertGreater(len(request_json), 0)

    def test_booking_view_post_with_valid_payload(self):
        """Ensure that instance can be create on post request."""
        url_base_name = reverse('bookings-api-list')
        request_post = self.client.post(
            url_base_name, self.payload, content_type="application/json; charset=utf8")
        self.assertEqual(request_post.status_code, status.HTTP_201_CREATED)

    def test_booking_view_delete_instance(self):
        """Ensure that instance can be deleted on delete request."""
        url_base_name = reverse('bookings-api-detail', args=[1])
        request_delete = self.client.delete(url_base_name)
        self.assertEqual(request_delete.reason_phrase, 'No Content')
        self.assertEqual(request_delete.status_code,
                         status.HTTP_204_NO_CONTENT)
