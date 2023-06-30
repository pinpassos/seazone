import locale

from rest_framework import serializers

from khanto.models import Announcement, Booking, Property


class PropertySerializer(serializers.ModelSerializer):
    """Property serializer ModelSerializer."""
    class Meta:
        """."""
        model = Property
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    """Announcement serializer ModelSerializer."""
    class Meta:
        """."""
        model = Announcement
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """Booking serializer ModelSerializer."""
    total_price = serializers.SerializerMethodField()

    class Meta:
        """."""
        model = Booking
        fields = '__all__'
        depth = 2

    def get_total_price(self, obj):
        """Convert total_price value to brl currency format."""
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        total_price = locale.currency(
            obj.total_price, grouping=True, symbol=None)
        return total_price
