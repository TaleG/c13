from django.db import models
from users.models import UserGroup, UserProfile

# Create your models here.

class Asset(models.Model):
    STATUS_CHOICES = (
        ('In use', 'In use'),
        ('Out of use', 'Out of use'),
    )
    TYPE_CHOICES = (
        ('Server', 'Server'),
        ('VM', 'VM'),
        ('Storage', "Storage"),
        ('Openstack','Openstack'),
        ('Openstack2','Openstack二期'),
    )
    ENV_CHOICES = (
        ('Prod', 'Production'),
        ('Test', 'Testing'),
    )

    # Important
    ip = models.GenericIPAddressField(max_length=32, verbose_name='IP', db_index=True)
    other_ip = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"其他IP")
    hostname = models.CharField(max_length=128, unique=True, verbose_name='Hostname')
    port = models.IntegerField(default=22, verbose_name='Port')
    groups = models.ManyToManyField(UserGroup, blank=True,
                                    verbose_name='Asset groups')
    admin_user = models.ForeignKey(UserProfile, null=True, blank=True,
                                   on_delete=models.SET_NULL, verbose_name="Admin user")
    system_users = models.CharField(blank=True,null=True,max_length=64,
                                          verbose_name="System User")
    idc = models.ForeignKey('IDC', blank=True, null=True,
                            on_delete=models.SET_NULL, verbose_name='IDC')
    is_active = models.BooleanField(default=True, verbose_name='Is active')
    type = models.CharField(choices=TYPE_CHOICES, max_length=16, blank=True, null=True,
                            default='Server', verbose_name='Asset type')
    env = models.CharField(choices=ENV_CHOICES, max_length=8, blank=True, null=True,
                           default='Prod', verbose_name='Asset environment')
    status = models.CharField(choices=STATUS_CHOICES, max_length=12, null=True, blank=True,
                              default='In use', verbose_name='Asset status')

    # Collect
    vendor = models.CharField(max_length=64, null=True, blank=True, verbose_name='Vendor')
    model = models.CharField(max_length=54, null=True, blank=True, verbose_name='Model')
    sn = models.CharField(max_length=128, null=True, blank=True, verbose_name='Serial number')

    cpu_model = models.CharField(max_length=64, null=True, blank=True, verbose_name='CPU model')
    cpu_count = models.IntegerField(null=True, verbose_name='CPU count')
    cpu_cores = models.IntegerField(null=True, verbose_name='CPU cores')
    memory = models.CharField(max_length=64, null=True, blank=True, verbose_name='Memory')
    disk_total = models.CharField(max_length=1024, null=True, blank=True, verbose_name='Disk total')
    disk_cloud = models.CharField(max_length=1024, null=True, blank=True, verbose_name='Disk cloud')

    os = models.CharField(max_length=128, null=True, blank=True, verbose_name='OS')
    os_version = models.CharField(max_length=16, null=True, blank=True, verbose_name='OS version')
    os_arch = models.CharField(max_length=16, blank=True, null=True, verbose_name='OS arch')

    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Date created')
    comment = models.TextField(max_length=128, default='', blank=True, verbose_name='Comment')

    def __unicode__(self):
        return '%s <%s: %s>' % (self.hostname, self.ip, self.port)
    __str__ = __unicode__


class IDC(models.Model):
    name = models.CharField(max_length=32, verbose_name='Name')
    bandwidth = models.CharField(
        max_length=32, blank=True, verbose_name='Bandwidth')
    contact = models.CharField(
        max_length=128, blank=True, verbose_name='Contact')
    phone = models.CharField(max_length=32, blank=True,
                             verbose_name='Phone')
    address = models.CharField(
        max_length=128, blank=True, verbose_name="Address")
    intranet = models.TextField(blank=True, verbose_name='Intranet')
    extranet = models.TextField(blank=True, verbose_name='Extranet')
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name='Date created')
    operator = models.CharField(
        max_length=32, blank=True, verbose_name='Operator')
    created_by = models.CharField(
        max_length=32, blank=True, verbose_name='Created by')
    comment = models.TextField(blank=True, verbose_name='Comment')

    def __unicode__(self):
        return self.name
    __str__ = __unicode__

