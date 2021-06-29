from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from OAUser.models import OAUser
from SongInfomation.models import Infomation


class Comment(models.Model):
    # content_type=models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
    # object_id=models.PositiveIntegerField()
    # content_object=GenericForeignKey('content_type','object_id')

    user=models.ForeignKey(OAUser,on_delete=models.DO_NOTHING)#你删你的,（外键）不管你

    #content_object = models.CharField(max_length=32)
    comment_time = models.DateTimeField(auto_now_add=True)
    text=models.TextField()

    code=models.ForeignKey(Infomation,on_delete=models.DO_NOTHING)


    class Mete:
        ordering=['comment_time']

