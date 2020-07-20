from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.BigIntegerField(null=True)
    address = models.TextField()

    def __str__(self):
        return self.name

