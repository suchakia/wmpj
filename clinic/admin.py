from django.contrib import admin

# Register your models here.
from .models import Clinic

class ClinicAdmin(admin.ModelAdmin):
    list_display = ['patient_name','patient_phone','patinet_address']
    list_filter  = ['patinet_address','patient_case','doctor']
    search_fields = ['patient_name']
admin.site.register(Clinic, ClinicAdmin)