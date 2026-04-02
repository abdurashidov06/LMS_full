from django.db import models

from lms_apps.base_models.base_model import BaseModel


class Auditory(BaseModel):
    room=models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.room}"