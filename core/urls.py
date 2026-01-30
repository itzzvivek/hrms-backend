from django.urls import path
from .views import *

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<str:employee_id>/', EmployeeDelete.as_view(), name='employee-delete'),
    path('attendance/', AttendanceCreate.as_view(), name='attendance-create'),
    path('attendance/list/', AttendanceList.as_view(), name='attendance-list'),
]