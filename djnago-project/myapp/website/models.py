from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_college = models.CharField(max_length=50)
    student_age = models.IntegerField()
    student_is_active = models.BooleanField(default=False)
    student_record_created = models.DateTimeField(auto_now=True)
    student_image = models.ImageField(upload_to='images/')
