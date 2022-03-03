from django.contrib import admin

# Register your models here.
from core.models import Appointment, Reviews

admin.site.register(Appointment)
admin.site.register(Reviews)
