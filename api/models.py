from django.db import models

# Create your models here.


class Invoice(models.Model):
    clientName = models.CharField(max_length=200, null=False, blank=False)
    clientEmail = models.EmailField(max_length=254, null=False, blank=False)
    clientAddress = models.TextField(null=False, blank=False)
    clientGSTNum = models.CharField(max_length=50, null=False, blank=False)
    billerName = models.CharField(max_length=200, null=False, blank=False)
    billerEmail = models.EmailField(max_length=254, null=False, blank=False)
    billerAddress = models.TextField(null=False, blank=False)
    billerGSTNum = models.CharField(max_length=50, null=False, blank=False)
    servicesDetails = models.JSONField(null=False, blank=False)
    taxRate = models.DecimalField(max_digits=4, decimal_places=2)
    bankAccDetails = models.TextField(null=False, blank=False)

    """ def __str__(self):
        return self """
