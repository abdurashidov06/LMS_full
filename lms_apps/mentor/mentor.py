from django.db import models

from lms_apps.base_models.base_user import UserModel


class Mentor(UserModel):
    user=models.OneToOneField(on_delete=models.CASCADE,related_name="user_student")
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.fathers_name}"

