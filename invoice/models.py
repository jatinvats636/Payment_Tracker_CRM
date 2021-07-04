from django.db import models
from client.models import Client, ClientService


class Invoice(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    gst = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return f"{self.client} {self.pk}"


class InvoiceService(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    service = models.ForeignKey(to=ClientService, on_delete=models.CASCADE)
    count = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return f"{self.service} {self.pk}"
