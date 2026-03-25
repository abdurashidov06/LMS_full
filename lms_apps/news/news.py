from django.db import models

from lms_apps.base_models.base_model import BaseModel


class NewsCategory(BaseModel):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class News(BaseModel):
    category=models.ForeignKey(NewsCategory,on_delete=models.CASCADE,related_name='category-news')
    name=models.CharField(max_length=100)
    about=models.TextField()
    image=models.ImageField(upload_to='images/news/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.image} {self.name}'

