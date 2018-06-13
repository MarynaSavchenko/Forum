from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cathegory(models.Model):

    name = models.CharField(max_length = 30, unique = True)
    description = models.CharField(max_length = 100, null = True)

    def __str__(self):
        return self.name

    def count_posts(self):
        return Post.objects.filter(topic__cathegory = self).count()

    def last_post(self):
        return Post.objects.filter(topic__cathegory = self).order_by('-created_at').first()



class Topic(models.Model):

    subject = models.CharField(max_length = 125)
    last_updated = models.DateTimeField(auto_now_add = True)
    cathegory = models.ForeignKey(Cathegory, related_name = 'topics')
    creater = models.ForeignKey(User, null=True, related_name = 'topics')

    def __str__(self):
        return self.subject

class Post(models.Model):

    message = models.CharField(max_length = 200)
    topic = models.ForeignKey(Topic, related_name = 'posts')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(null = True)
    creater = models.ForeignKey(User, null = True, related_name = 'posts')
    updater = models.ForeignKey(User, null = True, related_name = 'updater')

    def __str__(self):
        return self.message
