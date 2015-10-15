from django.contrib import admin

# Register your models here.
from .models import Volunteer, Village, Camp, Family, Fund

class VolunteerAdmin(admin.ModelAdmin):
	list_display = ("name","address","contact","email", "working_hrs")
	search_fields = ["name"]
	ordering = ["name"]

class VillageAdmin(admin.ModelAdmin):
	list_display = ("name", "adoption_date", "family_count", "block")

class CampAdmin(admin.ModelAdmin):
	list_display = ('village', 'camp_type', 'date', 'strt_time', 'end_time', 'details')

class FamilyAdmin(admin.ModelAdmin):
	list_display = ('village', 'head_name', 'address', 'income', 'members_count')

class FundAdmin(admin.ModelAdmin):
	list_display = ('source', 'receiving_date', 'amount', 'net_bal')

admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Village, VillageAdmin)
admin.site.register(Camp, CampAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Fund, FundAdmin)