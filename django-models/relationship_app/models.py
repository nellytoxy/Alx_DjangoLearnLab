from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE, names='books')
    
class Library(models.Model):
    name = models.CharField(max_length=200)
    book = models.ManyToManyField(Book)
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    