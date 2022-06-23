from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=90)
    website = models.CharField(max_length=90)