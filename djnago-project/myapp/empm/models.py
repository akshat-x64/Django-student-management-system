from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=50)
    employee_address = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=50)
    employee_phone = models.IntegerField()
    employee_working = models.BooleanField(default=False)
    employee_department = models.CharField(max_length=50)
    employee_record_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_name
