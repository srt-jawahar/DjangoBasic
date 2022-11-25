from django.db import models

# Create your models here.


class Player(models.Model):
    playerName = models.CharField(max_length=20)
    runs = models.FloatField(default= 0)
    team = models.CharField(max_length=20)
    records = models.TextField()

    def __str__(self) -> str:
        return self.playerName
