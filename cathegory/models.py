from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cathegory(models.Model):

    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name



class Topic(models.Model):

    subject = models.CharField(max_length=125)
    last_updated = models.DateTimeField(auto_now_add=True)
    cathegory = models.ForeignKey(Cathegory)
    starter = models.ForeignKey(User)

    def __str__(self):
        return self.subject

class Post(models.Model):

    message = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    creator = models.ForeignKey(User, related_name='creator')
    updater = models.ForeignKey(User, null=True, related_name='updater')
