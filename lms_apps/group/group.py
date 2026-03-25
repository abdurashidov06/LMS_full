from django.db import models
from multiselectfield import MultiSelectField

from lms_apps.auditory.classroom import Auditory
from lms_apps.base_models.base_model import BaseModel
from lms_apps.course.course import Course
from lms_apps.language.language import Language
from lms_apps.mentor.mentor import Mentor


class Group(BaseModel):
    class StudyDays(models.TextChoices):
        MONDAY = 'MON', 'Dushanba'
        TUESDAY = 'TUE', 'Seshanba'
        WEDNESDAY = 'WED', 'Chorshanba'
        THURSDAY = 'THU', 'Payshanba'
        FRIDAY = 'FRI', 'Juma'
        SATURDAY = 'SAT', 'Shanba'
        SUNDAY = 'SUN', 'Yakshanba'

    class StudyType(models.TextChoices):
        ONLINE='ONL', 'Onlayn'
        OFFLINE='OFL', 'Oflayn'

    name=models.CharField(max_length=300)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='groups')
    mentor=models.ForeignKey(Mentor,on_delete=models.SET_NULL, null=True, related_name='mentor-groups')
    support=models.ForeignKey(Mentor,on_delete=models.SET_NULL, null=True,related_name='support-groups')
    study_days = MultiSelectField(choices=StudyDays.choices)
    start_date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    classroom=models.ForeignKey(Auditory,on_delete=models.PROTECT,related_name='auditory-groups')
    language=models.ForeignKey(Language,on_delete=models.SET_NULL,related_name='language-groups')
    study_type=models.CharField(
        max_length=3,
        choices=StudyType.choices,
        default=StudyType.OFFLINE)


    def __str__(self):
        return f"{self.name} - {self.course}"



