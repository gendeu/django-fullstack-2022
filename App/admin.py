from django.contrib import admin
from App.models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','gender','created_at']
    search_fields = ['name','phone','email','gender']
    list_per_page = 10

admin.site.register(Patient, PatientAdmin)