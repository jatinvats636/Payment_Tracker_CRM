from django.db import models


def last_account_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return 'employee/{name}_{number}_last.{ext}'.format(name=instance.name, number=instance.mobile_number, ext=ext)


def second_last_account_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return 'employee/{name}_{number}_second_last.{ext}'.format(name=instance.name, number=instance.mobile_number, ext=ext)


class Account(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    balance = models.CharField(max_length=50)
    # last_records
    last_record = models.FileField(
        upload_to=last_account_upload_to, blank=True)
    second_last_record = models.FileField(
        upload_to=second_last_account_upload_to, blank=True)
