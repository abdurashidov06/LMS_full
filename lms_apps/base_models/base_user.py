from django.db import models

from lms_apps.location.locations import Region,District


class UserModel(models.Model):
    class Gender(models.TextChoices):
        MAN='MAN','Erkak'
        WOMAN='WMN','Ayol'

    image=models.ImageField(upload_to="files/user_profile_pics/",null=True,blank=True)
    surname = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    fathers_name = models.CharField(max_length=150)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL,null=True,blank=True, related_name='region_staff')
    district = models.ForeignKey(District, on_delete=models.SET_NULL,null=True,blank=True, related_name='city_staff')
    location = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(
        max_length=3,
        choices=Gender.choices,
        default=Gender.MAN
    )
    passport = models.CharField(unique=True)
    phone_number = models.PhoneNumberField(region='UZ', unique=True)
    extra_phone_number = models.PhoneNumberField(region='UZ', unique=True,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True