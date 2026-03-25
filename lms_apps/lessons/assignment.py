from django.db import models

from lms_apps.base_models.base_model import BaseModel
from lms_apps.lessons.lessons import Lessons


class Assignment(BaseModel):
    lesson=models.ForeignKey(Lessons,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    description=models.TextField()
    due_data=models.DateTimeField(blank=True,null=True)
    max_score=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

