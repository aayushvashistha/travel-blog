from django.db import models
from datetime import datetime

# Create your models here.

class item(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    heading = models.CharField(max_length=25)
    text = models.CharField(max_length=10000)


class blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    # def __str__(self):
    #     return self.title