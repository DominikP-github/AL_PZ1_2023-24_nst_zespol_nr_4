from django.db import models
from datetime import datetime

class Instrukcje(models.Model):
  id = models.IntegerField(primary_key=True)
  slowo_kluczowe = models.CharField(max_length=255)
  opis = models.CharField(max_length=255)

  def __str__(self):
    return str(self.id) + " " + self.slowo_kluczowe
  