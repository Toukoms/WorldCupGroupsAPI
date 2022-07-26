from django.db import models
from django.utils.text import slugify

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.TextField()
    pays = models.CharField(max_length=50, blank=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
