from enum import unique

from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ad_images', null=True, blank=True)


class Comment(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

