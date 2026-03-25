from django.db import models

from lms_apps.location.locations import Region,District


class UserModel(models.Model):
    class Gender(models.TextChoices):
        MAN='MAN','Erkak'
        WOMAN='WMN','Ayol'

    surname = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    fathers_name = models.CharField(max_length=150)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, related_name='region-staff')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, related_name='city-staff')
    birthday = models.DateField()
    gender = models.CharField(
        max_length=3,
        choices=Gender.choices,
        default=Gender.MAN
    )
    passport = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    extra_phone_number = models.CharField(max_length=20)
    location=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True