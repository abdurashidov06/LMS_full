from django.db import models

from lms_apps.base_models.base_model import BaseModel
from lms_apps.course.course import CourseModule

class LessonCategory(BaseModel):
    name=models.CharField(max_length=100)


class Lessons(BaseModel):
    LESSON_TYPE=[{"live":"Jonli dars"},{"online":"Onlayn"}]

    course=models.ForeignKey(CourseModule,on_delete=models.SET_NULL,related_name='course-lesson')
    lesson_category=models.ForeignKey(LessonCategory,on_delete=models.SET_NULL,related_name='category-lesson')
    name=models.CharField(max_length=100)
    order=models.IntegerField()
    lesson_type=models.CharField(max_length=30,choices=LESSON_TYPE)
    online_lesson=models.URLField(blank=True)
    video=models.FileField(blank=True)

    def __str__(self):
        return f"{self.lesson_category} - {self.name}"




