from datetime import date

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status


class AnnouncementViewTestCase(TestCase):
    fixtures = ['properties_fixtures', 'announcements_fixtures']

    def setUp(self):
        self.client = Client()
        self.payload = {
            "property": {
                "code": "p-1",
                "number_of_guests": 6,
                "number_of_bathrooms": 2,
                "allowed_pet": True,
                "cleaning_cost": 33.0,
                "activation_date": date(2023, 3, 3)
            },
            "plataform_name": "EARTHBNB",
            "plataform_rate": 150.0
        }


    def test_announcement_view_get_list_response(self):
        """Ensure get list method returns correct data."""
        url_base_name = reverse('announcements-api-list')
        request_get = self.client.get(url_base_name)
        request_json = request_get.json()
        self.assertEqual(request_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(request_json, list)
        self.assertGreater(len(request_json), 0)

    def test_announcement_view_get_detail_response(self):
        """Ensure get detail method returns correct data."""
        url_base_name = reverse('announcements-api-detail', args=[1])
        request_get = self.client.get(url_base_name)
        request_json = request_get.json()
        self.assertEqual(request_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(request_json, dict)
        self.assertGreater(len(request_json), 0)

    def test_announcement_view_post_with_valid_payload(self):
        """Ensure that instance can be create on post request."""
        url_base_name = reverse('announcements-api-list')
        request_post = self.client.post(
            url_base_name, self.payload, content_type="application/json; charset=utf8")
        self.assertEqual(request_post.status_code, status.HTTP_201_CREATED)

    def test_announcement_view_delete(self):
        """Ensure method delet is not allowed."""
        url_base_name = reverse('announcements-api-detail', args=[1])
        request_get = self.client.delete(url_base_name)
        self.assertEqual(request_get.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)