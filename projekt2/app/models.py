from django.db import models
from django.contrib.auth.models import User
  
class Keyword(models.Model):
    word = models.CharField(max_length=180, unique=True)
    opis_wyniku = models.TextField(default="fsdfsdf")

    def __str__(self):
        return self.word

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sentence = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.sentence} ({self.timestamp})"

class YourModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name