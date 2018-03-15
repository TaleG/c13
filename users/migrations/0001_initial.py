# Generated by Django 2.0.3 on 2018-03-14 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='Email')),
                ('role', models.CharField(blank=True, choices=[('Admin', 'Administrator'), ('User', 'User')], default='User', max_length=10, verbose_name='Role')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='Avatar')),
                ('wechat', models.CharField(blank=True, max_length=128, verbose_name='Wechat')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('valid_begin_time', models.DateTimeField(default=django.utils.timezone.now, help_text='yyyy-mm-dd HH:MM:SS')),
                ('valid_end_time', models.DateTimeField(blank=True, help_text='yyyy-mm-dd HH:MM:SS', null=True)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.UserGroup', verbose_name='User group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
