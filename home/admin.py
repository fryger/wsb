from django.contrib import admin
from .models import Organization, User, Car, Gps, Maintenance, CarService, Attachments

admin.site.register(Car)
admin.site.register(Gps)
admin.site.register(Organization)
admin.site.register(User)
admin.site.register(Maintenance)
admin.site.register(CarService)
admin.site.register(Attachments)
# admin.site.register(OrgSettings)
