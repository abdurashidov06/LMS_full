from django.db import models

from lms_apps.base_models.base_model import BaseModel


class RoleCategory(BaseModel):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Role(BaseModel):
    category=models.ForeignKey(RoleCategory,on_delete=models.CASCADE,related_name='category_role')
    name=models.CharField(max_length=150)


    def __str__(self):
        return f'{self.name}'