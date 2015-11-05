from django.contrib import admin

# Register your models here.
from .models import Volunteer, Village, Camp, Family, Fund, UserProfile

class VolunteerAdmin(admin.ModelAdmin):
	list_display = ("id","name","address","contact","email", "working_hrs", "joining_date")
	search_fields = ["name"]
	ordering = ["name"]
	prepopulated_fields = {'slug':('name',)}

class VillageAdmin(admin.ModelAdmin):
	list_display = ("id","name", "adoption_date", "family_count", "block")
	ordering = ["name"]
	prepopulated_fields = {'slug':('name',)}

class CampAdmin(admin.ModelAdmin):
	list_display = ("id",'village', 'camp_type', 'date', 'strt_time', 'end_time', 'organising_cost', 'details')
	ordering = ["village"]
	prepopulated_fields = {'slug':('camp_type',)}

class FamilyAdmin(admin.ModelAdmin):
	list_display = ("id",'village', 'head_name', 'father_name', 'address', 'income', 'members_count', 'prob_list')
	ordering = ["village"]
	prepopulated_fields = {'slug':('head_name',)}

class FundAdmin(admin.ModelAdmin):
	list_display = ("id",'source', 'receiving_date', 'amount', 'net_bal')
	ordering = ["source"]
	prepopulated_fields = {'slug':('source',)}

admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Village, VillageAdmin)
admin.site.register(Camp, CampAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Fund, FundAdmin)
admin.site.register(UserProfile)