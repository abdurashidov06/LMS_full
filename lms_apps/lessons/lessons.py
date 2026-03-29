from django.db import models

from lms_apps.base_models.base_model import BaseModel
from lms_apps.course.course import CourseModule

class LessonCategory(BaseModel):
    name=models.CharField(max_length=100)


class Lesson(BaseModel):
    LESSON_TYPE = [
        ("live", "Jonli dars"),
        ("online", "Onlayn"),
    ]

    course=models.ForeignKey(CourseModule,on_delete=models.SET_NULL,blank=True,null=True,related_name='course_lesson')
    lesson_category=models.ForeignKey(LessonCategory,on_delete=models.SET_NULL,blank=True,null=True,related_name='category_lesson')
    name=models.CharField(max_length=100)
    order=models.IntegerField()
    lesson_type=models.CharField(max_length=30,choices=LESSON_TYPE)
    online_lesson=models.URLField(blank=True,null=True,)
    video=models.FileField(upload_to="videos/lesson",blank=True,null=True,)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.lesson_category} - {self.name}"




