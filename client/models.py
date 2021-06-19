from django.db import models


def client_upload_to(instance, filename):
    return 'static/media/client/{filename}'.format(filename=filename)


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    # Profile Pic
    image = models.ImageField(upload_to=client_upload_to, blank=True)
    # Account Details
    account_holder_name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=50)
    MCIR_code = models.CharField(max_length=50)
    IFSC_code = models.CharField(max_length=50)
    name_of_bank = models.CharField(max_length=150)
    client_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.mobile_number}"


class ClientAddress(models.Model):
    owner = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    postal_pin_code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.owner.id} {self.street_address} {self.postal_pin_code}"
