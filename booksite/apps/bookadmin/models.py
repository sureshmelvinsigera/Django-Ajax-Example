from django.db import models


# Create your models here.
class BookModel(models.Model):
	title = models.CharField(max_length=50)
	publisher = models.CharField(max_length=50)
	author = models.CharField(max_length=30, blank=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	pages = models.IntegerField(blank=True, null=True)
