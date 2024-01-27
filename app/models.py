from django.db import models
from django.contrib.auth.models import User
  
class Slowa(models.Model):
    slowo = models.CharField(max_length=180, unique=True)
    opis_wyniku = models.TextField(default="")

    def __str__(self):
        return self.slowo

class Historia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sentence = models.CharField(max_length=255)
    opis = models.TextField(blank=True, null=True)
    czas = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.sentence} ({self.czas})"

class Fromularz(models.Model):
    Imie = models.CharField(max_length=100)
    email = models.EmailField()
    Problem = models.TextField()

    def __str__(self):
        return self.Imie