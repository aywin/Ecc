# from datetime import timezone
from django.db import models


class Eleve(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

#     ide = models.CharField(max_length=100, unique=False)  # Champ d'identification automatique pour les élèves

# class Alumni(models.Model):
#     nom = models.CharField(max_length=100)
#     prenom = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     ida = models.CharField(primary_key=True)  # Champ d'identification automatique pour les anciens élèves

# class MyModel(models.Model):
#     my_datetime_field = models.DateTimeField(default=timezone.now)
