from django.db import models

# Create your models here.

class Person(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20)
    birth = models.DateTimeField('date published')
    age = models.IntegerField()
