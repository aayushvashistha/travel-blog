from django.db import models
from datetime import datetime

# Create your models here.

class item(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    heading = models.CharField(max_length=25)
    text = models.CharField(max_length=10000)

    def __str__(self):
        return self.heading


class blog(models.Model):
    imageHomepage = models.ImageField(upload_to='images')
    imagePrimary = models.ImageField(upload_to='images')
    imageSecondary = models.ImageField(upload_to='images', null=True)
    title = models.CharField(max_length=1000)
    topicIntro_head = models.CharField(max_length=100, null=False)
    topicIntro_body = models.TextField(null=False)
    mainTopic_head = models.CharField(max_length=100, null=False)
    main_body = models.TextField(null=False)
    subtopic_head = models.CharField(max_length=100, null=True)
    subtopic_body = models.TextField(max_length=1000, null=True)
    created_by = models.CharField(max_length=30, null=False)
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
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fullname