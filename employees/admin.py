from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'salary', 'designation', 'description')
    search_fields = ('name', 'address', 'designation')
