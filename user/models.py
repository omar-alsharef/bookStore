from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.userName
