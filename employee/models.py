from django.db import models


def employee_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return 'employee/{name}_{number}.{ext}'.format(name=instance.name, number=instance.mobile_number, ext=ext)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
    salary = models.CharField(max_length=20)
    joining_date = models.DateField()
    description = models.CharField(max_length=100)
    # Account details
    account_holder_name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=50)
    MCIR_code = models.CharField(max_length=50)
    IFSC_code = models.CharField(max_length=50)
    name_of_bank = models.CharField(max_length=150)
    # Profile Pic
    image = models.ImageField(upload_to=employee_upload_to, blank=True)

    def __str__(self):
        return f"{self.name} {self.mobile_number}"
