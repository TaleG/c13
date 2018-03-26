#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from django import forms
from assets.models import Asset

class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset

        fields = [
            "ip", "other_ip", "hostname", "port", "groups", "admin_user", "system_users", "idc",
            "is_active", "type", "env", "status", "vendor", "model", "sn", "cpu_model", "cpu_count",
            "cpu_cores", "memory", "disk_total", "disk_cloud", "os", "os_version", "os_arch", "comment"
        ]