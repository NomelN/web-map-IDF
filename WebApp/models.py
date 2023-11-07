from django.db import models


# Create your models here.
class Localisation(models.Model):
    mairie = models.CharField(max_length=250)
    ville = models.CharField(max_length=250)
    adresse = models.CharField(max_length=250)
    code_postal = models.FloatField()
    departement = models.CharField(max_length=250)
    longitude = models.FloatField()
    latitude = models.FloatField()
    label_vvf = models.CharField(max_length=250)

    def __str__(self):
        return self.ville
