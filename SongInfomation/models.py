from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from OAUser.models import OAUser


class Infomation(models.Model):

    code=models.CharField(primary_key=True,max_length=100)
    photo_song_url=models.CharField(max_length=100)
    photo_face_url=models.CharField(max_length=100)
    photo_songer_url = models.CharField(max_length=100)
    words=models.TextField()
    song_time = models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    good=models.IntegerField()

    class Mete:
        ordering=['comment_time']

