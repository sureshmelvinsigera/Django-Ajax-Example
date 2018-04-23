from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_pages = models.IntegerField(blank=True, null=True)
