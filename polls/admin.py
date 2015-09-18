from django.contrib import admin

# Register your models here.
from .models import Volunteer, Village, Camp, Family, Fund

class VolunteerAdmin(admin.ModelAdmin):
	list_display = ["name","address","contact","email"]
	search_fields = ["name"]
	ordering = ["name"]

admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Village)
admin.site.register(Camp)
admin.site.register(Family)
admin.site.register(Fund)