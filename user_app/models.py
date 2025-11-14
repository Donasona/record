from django.db import models

# Create your models here.
class Recordmodel(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    mark = models.DecimalField(max_digits=6,decimal_places=2)