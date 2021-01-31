from rest_framework import routers
from .api import EmployeeViewset
from . import views
from django.urls import path, include


# use Default router from rest_framework
router = routers.DefaultRouter()
# Endpoints
router.register('api/employee', viewset=EmployeeViewset)

# it will gives us the urls that register in above endpoints.
#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls))
]
