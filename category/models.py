from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=50,default='')


    def __str__(self):
        return self.categoryName

