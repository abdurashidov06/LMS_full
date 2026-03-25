from django.db import models

from lms_apps.course.course import Course
from lms_apps.models import UserModel


class Student(UserModel):
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,related_name='course-student')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.fathers_name}"