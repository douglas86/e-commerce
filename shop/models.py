from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discounted = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Storage(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
