from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now=True)
