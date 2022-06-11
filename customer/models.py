from django.db import models

# Create your models here.
class Customer(models.Model):
    customerName = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()


    def __str__(self):
        return self.customerName