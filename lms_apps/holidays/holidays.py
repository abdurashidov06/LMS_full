from django.db import models

from lms_apps.base_models.base_model import BaseModel


class Holidays(BaseModel):
    title=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return f"{self.title}"