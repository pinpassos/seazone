from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response

from khanto.models import Announcement, Booking, Property
from khanto.serializers import (AnnouncementSerializer, BookingSerializer,
                                PropertySerializer)


class PropertyViewSet(viewsets.ModelViewSet):
    """Returns response of Property API."""
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    """
    Returns response of Announcement API."""
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    http_method_names = ['get', 'post', 'head', 'put', 'patch', 'options']


class BookingViewSet(viewsets.ModelViewSet):
    """Returns response of Booking API."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    http_method_names = ['get', 'post', 'delete', 'head', 'options']

    def create(self, request, *args, **kwargs):
        request_data = request.data
        check_in = request_data.get('check_in')
        check_out = request_data.get('check_out')

        if check_in > check_out:
            return Response({'error': 'Check-in cannot be greater than check-out date'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
