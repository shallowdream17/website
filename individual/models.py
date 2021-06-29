from django.db import models

# Create your models here.
from OAUser.models import OAUser
from SongInfomation.models import Infomation


class individual(models.Model):


    user=models.ForeignKey(OAUser,on_delete=models.DO_NOTHING)
    code = models.ForeignKey(Infomation, on_delete=models.DO_NOTHING)
    comment_time = models.DateTimeField(auto_now_add=True)
    once_good=models.IntegerField()
    title=models.CharField(max_length=200)

    class Mete:
        ordering=['comment_time']