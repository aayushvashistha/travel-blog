from django.db import models
from datetime import datetime

# Create your models here.

class item(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    heading = models.CharField(max_length=25)
    text = models.CharField(max_length=10000)


class blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class write(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.fullname