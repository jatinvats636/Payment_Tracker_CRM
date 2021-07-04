from django.db import models
from invoice.models import Invoice

# Create your models here.


class CreditNotes(models.Model):
    invoice=models.OneToOneField(to=Invoice,on_delete=models.CASCADE)
    created_at=models.DateTimeField()
    reason=models.CharField(max_length=1000,blank=False,null=False)
    payment_terms=models.CharField(max_length=500,blank=False,null=False)
    status=models.CharField(max_length=20,blank=False,null=False)

    def __str__(self):
        return f"{self.invoice} {self.pk}"

