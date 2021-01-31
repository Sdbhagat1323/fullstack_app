from rest_framework import serializers
from employee.models import Employee, Manager

# create serializer objects


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):

    # add the employee serialliser
    employee_model = EmployeeSerializer()

    class Meta:
        model = Manager
        fields = '__all__'

    def join(self, validated_data):
        raw_data = validated_data.pop('employee_model')
        manager_model = Manager.objects.create(**validated_data)
        Employee.objects.create(manager_model, **raw_data)
        return manager_model
