# -*- coding: utf-8 -*-
from django.contrib import admin
from doctor_rj.models import Establishment, UnitType, Administrative, OrganizationNature, TeachingActivity

class EstablishmentAdmin(admin.ModelAdmin):
	list_display = ('common_name', 'district' )
	search_fields = ('common_name', )

admin.site.register(Establishment, EstablishmentAdmin)
admin.site.register(UnitType)
admin.site.register(Administrative)
admin.site.register(OrganizationNature)
admin.site.register(TeachingActivity)