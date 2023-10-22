from django.db import models
from django.db.models import Model

class Thing(Model):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()
