from django.contrib import admin
from assets import models
# Register your models here.

class AssetAdmin(admin.ModelAdmin):
    list_display = ('ip','hostname','idc','status')

class IDCAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone','date_created')

admin.site.register(models.Asset,AssetAdmin)
admin.site.register(models.IDC,IDCAdmin)
