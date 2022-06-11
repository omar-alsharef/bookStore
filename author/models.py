import datetime
from django.db import models

from nationality.models import Nationality

# Create your models here.
class Author(models.Model):
    authorName = models.CharField(max_length=50,default='')
    nationality = models.ForeignKey(Nationality,on_delete=models.CASCADE,default='')
    bornDate = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.authorName