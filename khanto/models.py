import uuid

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

DAILY_PRICE = 250.00


class Property(models.Model):
    """Stores property entries."""
    code = models.CharField('Property code', max_length=3)
    number_of_guests = models.PositiveIntegerField(
        'Number of guests', help_text='Max number of guests', validators=[MinValueValidator(1)])
    number_of_bathrooms = models.PositiveIntegerField('Number of bathrooms')
    allowed_pet = models.BooleanField('Allowed pet')
    cleaning_cost = models.FloatField('Cleaning cost', validators=[MinValueValidator(
        0.0, 'The value of cleaning cost can not be a negative number.')])
    activation_date = models.DateField(
        'Activation date', blank=True, null=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        """."""
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        """."""
        return self.code


class Announcement(models.Model):
    """Stores announcement entries."""
    property = models.ForeignKey(
        'Property', related_name='announcements', on_delete=models.CASCADE)
    plataform_name = models.CharField('Plataform name', max_length=120)
    plataform_rate = models.FloatField(
        'Plataform rate', validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        """."""
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'

    def __str__(self):
        """."""
        return f'Announcemet of {self.property}'


class Booking(models.Model):
    """Stores booking entries."""
    code = models.UUIDField('Booking code', unique=True,
                            default=uuid.uuid4, editable=False)
    announcement = models.ForeignKey(
        'Announcement', on_delete=models.DO_NOTHING)
    check_in = models.DateField('Check-in date')
    check_out = models.DateField('Check-out date')
    total_price = models.FloatField('Total price', null=True, blank=True)
    number_of_guests = models.PositiveIntegerField('Number of guests')
    comment = models.TextField('Comment')
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        """."""
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def get_number_of_days(self):
        """Returns quantity days of booking."""
        number_of_days = (
            self.check_out - self.check_in).days if self.check_out != self.check_in else 1
        return number_of_days

    def get_total_price_per_guest(self):
        """Returns sum of the price based on the number of guests."""
        daily_price = DAILY_PRICE
        number_of_guests = self.number_of_guests
        total_price_per_guest = number_of_guests * daily_price
        return total_price_per_guest

    def get_total_price_per_guest_multiplied_by_days(self):
        """Returns price based on the number of guests multiplied by the number of days."""
        total_price_per_guest = self.get_total_price_per_guest()
        number_of_days = self.get_number_of_days()
        total_price_per_guest_multiplied_by_days = total_price_per_guest * number_of_days
        return total_price_per_guest_multiplied_by_days

    def calculate_total_price_of_booking(self):
        """Returns total price of booking after the calculations."""
        number_of_days = self.get_number_of_days()
        total_price_per_guest_multiplied_by_days = self.get_total_price_per_guest_multiplied_by_days()
        price_of_cleaning_cost_per_day = self.announcement.property.cleaning_cost * number_of_days
        price_of_plataform_rate = self.announcement.plataform_rate
        total_price_of_booking = total_price_per_guest_multiplied_by_days + \
            price_of_cleaning_cost_per_day + price_of_plataform_rate
        return total_price_of_booking

    def save(self, *args, **kwargs):
        """Override save method to calulate total price of booking before save instance."""
        self.total_price = self.calculate_total_price_of_booking()
        return super().save(*args, **kwargs)

    def clean(self):
        """Override clean method to validate fields based on business rules."""
        if self.check_in > self.check_out:
            raise ValidationError(
                message='Check-in cannot be greater than check-out date')

        if self.number_of_guests > self.announcement.property.number_of_guests:
            raise ValidationError(
                message='Number of guests cannot be greater than supported by the property')

    def __str__(self):
        """."""
        return str(self.code)
