from django.db import models
from django.utils import timezone


class Coms(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    group = models.ForeignKey('commapp.Coms')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    announce_date = models.DateTimeField(blank=True, null=None)

    def __str__(self):
        return self.title
