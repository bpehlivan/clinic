from django.contrib import admin

from doctors.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone_number", "specialization", "is_active")
    search_fields = ("full_name", "email", "phone_number", "specialization")
    list_filter = ("is_active", "specialization")
