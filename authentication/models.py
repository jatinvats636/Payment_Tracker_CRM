from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
    account_details = models.CharField(max_length=500)
    # image field upload_to path is not properly set, please ensure it before starting to upload pics
    image = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
    client_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.mobile_number}"


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # rate field: verify if this field is char or int
    rate = models.CharField(max_length=10)
    poc = models.CharField(max_length=20)
    other = models.CharField(max_length=100)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client} {self.title}"


class Invoice(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    # file field: not functional, work on upload_to
    file = models.FileField()


class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
    salary = models.CharField(max_length=20)
    joining_date = models.DateField()
    account_number = models.CharField(max_length=20)
    account_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    # image field: upload to path is not properly set, please ensure it before starting to upload pics
    image = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)


class Account(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    balance = models.CharField(max_length=50)
    # last_record field: not functional, work on upload_to
    last_record = models.FileField()


# Check if "Session" name causes conflicts with any registered django app
class Session(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()


# __TODO__ :
# Create Employee_payments table, because for 1 employee there will be multiple payments
# Check how to handle invoices
# Create Credit_notes table, similar to Invoices
