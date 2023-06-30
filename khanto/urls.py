from django.urls import include, path
from rest_framework import routers

from khanto.views import PropertyViewSet, AnnouncementViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
