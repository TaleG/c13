#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from users import models
from django.forms import ModelForm
class UserProfileForm(ModelForm):

    class Meta:
        model = models.UserProfile
        fields = ['name', 'valid_begin_time', 'valid_end_time']