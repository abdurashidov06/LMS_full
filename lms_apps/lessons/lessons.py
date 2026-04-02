from django.db import models

from account.models import User
from lms_apps.base_models.base_model import BaseModel
from lms_apps.course.course import CourseModule




class Lesson(BaseModel):

    course=models.ForeignKey(CourseModule,on_delete=models.SET_NULL,blank=True,null=True,related_name='course_lesson')
    name=models.CharField(max_length=100)
    order=models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course} - {self.name}"

class LessonItem(BaseModel):
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name="lesson_lesson_item")
    content=models.TextField(blank=True,null=True)
    file=models.FileField(upload_to="files/lesson_files/",blank=True,null=True)
    video=models.FileField(upload_to="videos/lesson",blank=True,null=True)

    def __str__(self):
        return self.lesson


class LessonItemProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_item = models.ForeignKey(LessonItem, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)






