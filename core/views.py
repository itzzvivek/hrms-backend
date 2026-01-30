from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer


class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDelete(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    lookup_field = 'employee_id'

class AttendanceCreate(generics.CreateAPIView):
    serializer_class = AttendanceSerializer
        
class AttendanceList(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        qs = Attendance.objects.all()
        emp_id = self.request.query_params.get('employee_id')
        data = self.request.query_params.get('date')

        if emp_id:
            qs = qs.filter(employee__employee_id=emp_id)
        if data:
            qs = qs.filter(date=data)

        return qs