from django.contrib.auth.models import AbstractUser
from django.db import models

from lms_apps.base_models.base_model import BaseModel


class User(AbstractUser,BaseModel):
    class UserRole(models.TextChoices):
        STUDENT = "student" , "Student",
        ADMIN = "admin" , "Admin",
        MENTOR = "mentor" , "Mentor",
        STAFF = "staff" , "Staff"

    role=models.CharField(max_length=20,
                          choices=UserRole.choices,
                          default=UserRole.STUDENT
                          )

    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
