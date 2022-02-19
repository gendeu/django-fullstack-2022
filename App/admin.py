from django.contrib import admin
from App.models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','phone','email','age','gender','created_at']
    search_fields = ['firstname','lastname','phone','email','gender']
    list_filter = ['gender']
    list_per_page = 10

admin.site.register(Patient, PatientAdmin)