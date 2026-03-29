from django.db import models

from lms_apps.base_models.base_model import BaseModel


class Region(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(BaseModel):
    """Viloyatlar & Tumanlar —
    parent=None  →  Viloyat
    parent=<viloyat>  →  Tuman / Shahar
    """
    region = models.ForeignKey(
        Region,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='children',
        verbose_name="Viloyat (ota-region)"
    )
    name = models.CharField(max_length=200)   # translatable later
    latitude  = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)

    def __str__(self):
        return self.name
