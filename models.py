from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Work(models.Model):
    LINK_CHOICES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('Other', 'Other'),
    )
    link = models.CharField(max_length=255)
    work_type = models.CharField(max_length=10, choices=LINK_CHOICES)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)
