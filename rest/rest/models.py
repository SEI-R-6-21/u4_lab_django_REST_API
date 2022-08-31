from django.db import models

# Create your models here.

# tunr/models.py


class NFL_Teams(models.Model):
    team_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    wins = models.CharField(max_length=100)
    losses = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    nfl_team = models.ForeignKey(
        NFL_Teams, on_delete=models.CASCADE, related_name='player')
    name = models.CharField(max_length=100)
    postion = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    injured = models.CharField(max_length=100)

    def __str__(self):
        return self.name
