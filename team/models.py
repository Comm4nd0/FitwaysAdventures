from django.db import models

# Create your models here.

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=250)
    image = models.ImageField(blank=True)
    bio = models.TextField()

    facebook = models.CharField(max_length=250, blank=True)
    twitter = models.CharField(max_length=250, blank=True)
    linkedin = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name
