from django.contrib import admin
from .models import Employee, Attendance
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'full_name', 'email', 'department')
    search_fields = ('full_name', 'email', 'department')
    list_filter = ('department',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee', 'date', 'status')
    search_fields = ('employee__full_name', 'employee__email')
    list_filter = ('status', 'date')