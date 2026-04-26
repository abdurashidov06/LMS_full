from django.db import models

from account.models import User
from lms_apps.base_models.base_user import UserModel


class Mentor(UserModel):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_mentor")

    def __str__(self):
        return f"{self.name} - {self.fathers_name}"


