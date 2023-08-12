from django.contrib import admin
from empm import models
# Register your models here.


class empAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'employee_address')


admin.site.register(models.Employee, empAdmin)
