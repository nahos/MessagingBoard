from django.db import models
from django.conf import settings


class Board(models.Model):
    name = models.TextField(max_length=100, unique= True)
    description = models.TextField(max_length=200)
    def __str__(self):
        return self.name


class Posts(models.Model):
    class Meta:
        unique_together = ('name', 'board')
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=100000)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    board = models.ForeignKey(Board,related_name='posts',on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post_user',on_delete=models.CASCADE)


class Comments(models.Model):
    message = models.TextField()
    created_on = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments_user',on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,related_name='comments',on_delete=models.CASCADE)
