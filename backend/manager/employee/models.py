from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# we already got username, password fields


class Employee(models.Model):
    owner = models.ForeignKey(
        User, related_name="employee", on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    mobile = models.IntegerField()
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name


class Manager(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    company = models.CharField(max_length=100)


# Create your models here.
# const { firstName, lastName, email, mobile, date_of_birth,address, city, company };
