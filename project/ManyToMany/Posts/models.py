from django.db import models
from tag.models import Tag
# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=False, null=False)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)