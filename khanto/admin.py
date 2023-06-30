from django.contrib import admin

from khanto.models import Announcement, Booking, Property


class BookingAdmin(admin.ModelAdmin):
    """This class was created to set some specifics behaviors to booking admin."""
    readonly_fields = ('total_price',)
    list_display = ('code', 'announcement', 'check_in',
                    'check_out', 'number_of_guests', 'total_price')


admin.site.register(Booking, BookingAdmin)
admin.site.register(Property)
admin.site.register(Announcement)
