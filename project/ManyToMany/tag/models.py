from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.TextField(blank=False, null=False)
    body = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    post = models.ManyToManyField(Post, related_name='tags', blank=True)