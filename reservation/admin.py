from django.contrib import admin
from .models import Seat, Ticket
# Register your models here.

class SeatAdmin(admin.ModelAdmin):
    list_display = ('id',)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Ticket)
