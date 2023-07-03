from django.urls import include, path
from rest_framework import routers

from khanto.views import PropertyViewSet, AnnouncementViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='properties-api')
router.register(r'announcements', AnnouncementViewSet, basename='announcements-api')
router.register(r'bookings', BookingViewSet, basename='bookings-api')

urlpatterns = [
    path('api/', include(router.urls)),
]
