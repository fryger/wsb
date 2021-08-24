from django.contrib import admin
from .models import Organization, User, Car

admin.site.register(Car)
#admin.site.register(Gps)
admin.site.register(Organization)
admin.site.register(User)
#admin.site.register(OrgSettings)
