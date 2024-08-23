from django.db import models

# Create your models here.


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)
    factory_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.model} - {self.brand}"
