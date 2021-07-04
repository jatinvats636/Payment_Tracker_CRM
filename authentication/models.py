from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class CustomSessionModel(models.Model):
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    login_time=models.DateTimeField(null=True)
    logout_time=models.DateTimeField(null=True)
    is_active=models.BooleanField(default=True)