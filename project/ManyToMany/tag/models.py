from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True, primary_key=True)
    