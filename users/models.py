from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
    ROLE_ADMIN = 'Admin'
    ROLE_USER = 'User'

    ROLE_CHOICES = (
        (ROLE_ADMIN, 'Administrator'),
        (ROLE_USER, 'User'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=128, unique=True, verbose_name='Email')
    groups = models.ForeignKey('UserGroup', related_name='users', blank=True, verbose_name='User group',on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_CHOICES, default='User', max_length=10, blank=True, verbose_name='Role')
    avatar = models.ImageField(upload_to="avatar", blank=True, null=True, verbose_name='Avatar')
    wechat = models.CharField(max_length=128, blank=True, verbose_name='Wechat')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone')
    date_created = models.DateTimeField(auto_now_add=True, null=True,
                                        verbose_name='Date created')
    valid_begin_time = models.DateTimeField(default=timezone.now, help_text="yyyy-mm-dd HH:MM:SS")
    valid_end_time = models.DateTimeField(blank=True, null=True, help_text="yyyy-mm-dd HH:MM:SS")
    created_by = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name



class UserGroup(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name')
    comment = models.TextField(blank=True, verbose_name='Comment')
    date_created = models.DateTimeField(auto_now_add=True, null=True,
                                        verbose_name='Date created')
    created_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
