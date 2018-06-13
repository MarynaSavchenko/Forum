from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cathegory(models.Model):

    name = models.CharField(max_length = 30, unique = True)
    description = models.CharField(max_length = 100)

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
    creater = models.ForeignKey(User, related_name = 'topics')
    views = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.subject

    def count_posts(self):
        return Post.objects.filter(topic = self).count()-1


class Post(models.Model):

    message = models.CharField(max_length = 4000)
    topic = models.ForeignKey(Topic, related_name = 'posts')
    created_at = models.DateTimeField(auto_now_add = True)
    creater = models.ForeignKey(User, related_name = 'posts')

    def __str__(self):
        return self.message
