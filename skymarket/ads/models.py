from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=250, unique=True)
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # _now_add когда объект создан
    image = models.ImageField(upload_to='ad_images', null=True, blank=True)


class Comment(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

