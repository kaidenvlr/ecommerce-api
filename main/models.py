from django.contrib.auth.models import User
from django.db import models


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    number = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(upload_to='media/avatar', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
