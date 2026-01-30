from rest_framework import serializers
from .models import Employee, Attendance


class EmployeeSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'

from rest_framework import serializers
from .models import Employee, Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    # INPUT (for POST)
    employee_id = serializers.CharField(write_only=True)
    # OUTPUT (for GET)
    employee_code = serializers.CharField(
        source="employee.employee_id", read_only=True
    )
    employee_name = serializers.CharField(
        source="employee.full_name", read_only=True
    )

    class Meta:
        model = Attendance
        fields = [
            "id",
            "employee_id",    
            "employee_code",  
            "employee_name",  
            "date",
            "status",
        ]

    def validate(self, data):
        emp_id = data.get("employee_id")

        if not Employee.objects.filter(employee_id=emp_id).exists():
            raise serializers.ValidationError(
                {"employee_id": "Employee with this ID does not exist"}
            )

        return data

    def create(self, validated_data):
        emp_id = validated_data.pop("employee_id")
        employee = Employee.objects.get(employee_id=emp_id)

        attendance, created = Attendance.objects.get_or_create(
            employee=employee,
            date=validated_data["date"],
            defaults={"status": validated_data["status"]},
        )

        if not created:
            raise serializers.ValidationError(
                "Attendance already marked for this employee on this date"
            )

        return attendance
