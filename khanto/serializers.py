import locale

from rest_framework import serializers
from rest_framework.validators import ValidationError

from khanto.models import Announcement, Booking, Property


class PropertySerializer(serializers.ModelSerializer):
    """Property serializer ModelSerializer."""
    class Meta:
        """."""
        model = Property
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    """Announcement serializer ModelSerializer."""
    property = PropertySerializer()

    class Meta:
        """."""
        model = Announcement
        fields = '__all__'

    def create(self, validated_data):
        """Override create method to handle nested fields."""
        property = validated_data.pop('property')
        property_model, _ = Property.objects.get_or_create(**property)
        announcement_instance = Announcement.objects.create(
            property=property_model, **validated_data)
        return announcement_instance

    def update(self, instance, validated_data):
        """Override update method to handle nested fields."""
        property = validated_data.pop('property')
        instance.plataform_name = validated_data.get('plataform_name')
        instance.plataform_rate = validated_data.get('plataform_rate')

        property_of_instance = Property.objects.filter(**property).first()
        if property_of_instance:
            instance.property = property_of_instance
            return instance


class BookingSerializer(serializers.ModelSerializer):
    """Booking serializer ModelSerializer."""
    total_price = serializers.SerializerMethodField()
    announcement = AnnouncementSerializer()

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

    def create(self, validated_data):
        """Override create method to handle nested fields."""
        announcement_data = validated_data.pop('announcement')
        property_data = announcement_data.pop('property')

        property_instance, _ = Property.objects.get_or_create(**property_data)
        announcement_instance, _ = Announcement.objects.get_or_create(
            property=property_instance, **announcement_data)

        booking_instance = Booking.objects.create(
            announcement=announcement_instance, **validated_data)

        return booking_instance
