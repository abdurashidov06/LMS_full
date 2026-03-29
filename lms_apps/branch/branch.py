from django.db import models

from lms_apps.base_models.base_model import BaseModel
from lms_apps.location.locations import Region,District


class Branch(BaseModel):
    name = models.CharField(max_length=300)
    region=models.ForeignKey(Region,on_delete=models.PROTECT,related_name='region_branch')
    district=models.ForeignKey(District,on_delete=models.PROTECT,related_name='city_branch')
    location=models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)


    def __str__(self):
        return f"{self.name}"