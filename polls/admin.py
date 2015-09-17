from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Volunteer, Village, Camp, Family, Fund

admin.site.register(Volunteer)
admin.site.register(Village)
admin.site.register(Camp)
admin.site.register(Family)
admin.site.register(Fund)