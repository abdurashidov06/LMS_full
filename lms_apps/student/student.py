
from django.db import models

from lms_apps.base_models.base_user import UserModel
from lms_apps.group.group import Group


class Student(UserModel):
    user=models.OneToOneField(on_delete=models.CASCADE,related_name="user_student")
    group=models.ForeignKey(Group,on_delete=models.SET_NULL,null=True,blank=True,related_name='course_student')


    def __str__(self):
        return f"{self.name} - {self.fathers_name}"