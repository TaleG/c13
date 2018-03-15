from django.contrib import admin
from users import models
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name','email','role','wechat','date_created')

class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('name','comment','date_created')


admin.site.register(models.UserProfile,UserProfileAdmin)
admin.site.register(models.UserGroup,UserGroupAdmin)

