from django.db import models
from user_login.models import User


# Create your models here.
class Images(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='微信', max_length=64, null=True, blank=True)
    port = models.CharField(verbose_name='端口', max_length=64, default='8080')
    dir = models.CharField(verbose_name='目录', max_length=64, default='/var/lib')
    cpu = models.IntegerField(verbose_name='核心数', default=500)
    ram = models.IntegerField(verbose_name='内存', default=500)
    disk = models.IntegerField(verbose_name='硬盘', default=500)
