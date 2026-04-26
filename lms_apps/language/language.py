from django.db import models

from lms_apps.base_models.base_model import BaseModel


class Language(BaseModel):
    title=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    flag=models.FileField(
        upload_to='files/flags/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title