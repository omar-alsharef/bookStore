
from django.db import models
from author.models import Author
from category.models import Category

# Create your models here.
class Book(models.Model):
    bookName = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    isBorrow = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.bookName