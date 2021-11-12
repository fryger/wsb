from django.contrib import admin
from .models import CarDamages, CarDocuments, CarDamagesAttachment, Organization, Reminders, User, Car, Gps, Maintenance, CarService, Attachments, CarDriversHistory

admin.site.register(Car)
admin.site.register(Gps)
admin.site.register(Organization)
admin.site.register(User)
admin.site.register(Maintenance)
admin.site.register(CarService)
admin.site.register(Attachments)
admin.site.register(CarDriversHistory)
admin.site.register(CarDamages)
admin.site.register(CarDamagesAttachment)
admin.site.register(CarDocuments)
admin.site.register(Reminders)
# admin.site.register(OrgSettings)
