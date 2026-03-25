
from django.db import models

from lms_apps.base_models.base_model import BaseModel
from lms_apps.branch.branch import Branch


class Course(BaseModel):
    """Kurslar — """

    class PaymentType(models.TextChoices):
        MONTHLY = 'monthly', "Oylik to'lov"
        ONCE    = 'once',    "Bir martalik to'lov"

    name                  = models.CharField(max_length=300)
    academic_hours_lesson = models.PositiveIntegerField()
    academic_hours_total  = models.PositiveIntegerField()
    price                 = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type          = models.CharField(
        max_length=20,
        choices=PaymentType.choices,
        default=PaymentType.MONTHLY
    )
    branch                = models.ForeignKey(
        Branch, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='courses'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"




class CourseModule(BaseModel):
    """Kurs modullari — Image 18 (Modullar section)"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    name   = models.CharField(max_length=300)
    order  = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.course} — {self.title}"