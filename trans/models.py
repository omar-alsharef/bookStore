from django.db import models

from customer.models import Customer
from book.models import Book

# Create your models here.
class Trans(models.Model):
    bookName = models.ForeignKey(Book,on_delete=models.CASCADE,default=None)
    theCustomer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    borrowDate = models.DateField(blank=True, null=True)
    returnDate = models.DateField(blank=True, null=True)

