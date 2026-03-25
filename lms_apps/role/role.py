from django.db import models

from lms_apps.base_models.base_model import BaseModel


class RoleCategory(BaseModel):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Role(BaseModel):
    category=models.ForeignKey(RoleCategory,on_delete=models.CASCADE,related_name='category-role')
    name=models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'