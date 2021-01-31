from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer

# Create your views here.


def index(request):
    return render(request, 'frontend/myapp/public/index.html')


class EmployeeList(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    pass
