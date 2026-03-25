from django.db import models

from lms_apps.branch.branch import Branch
from lms_apps.models import UserModel
from lms_apps.role.role import Role


class Staff(UserModel):
    position=models.CharField(max_length=100)
    branch=models.ForeignKey(Branch,on_delete=models.SET_NULL,related_name='branch-staff')
    role=models.ForeignKey(Role,on_delete=models.SET_NULL,related_name='role-staff')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.fathers_name} - {self.role}"


