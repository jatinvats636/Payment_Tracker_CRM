from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    # image field upload_to path is not properly set, please ensure it before starting to upload pics
    image = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
    #Account Details
    account_holder_name=models.CharField(max_length=200)
    account_number=models.CharField(max_length=50)
    MCIR_code=models.CharField(max_length=50)
    IFSC_code=models.CharField(max_length=50)
    name_of_bank=models.CharField(max_length=150)
    client_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.mobile_number}"


class ClientAddress(models.Model):
    owner=models.ForeignKey(to=Client,on_delete=models.CASCADE)
    street_address=models.CharField(max_length=300)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    postal_pin_code=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.owner.id} {self.street_address} {self.postal_pin_code}"

