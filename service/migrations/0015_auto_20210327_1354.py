# Generated by Django 3.1.5 on 2021-03-27 10:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0014_tracking_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerbill',
            name='user_id',
        ),
        migrations.AddField(
            model_name='customerbill',
            name='user_id',
            field=models.ManyToManyField(blank=True, null=True, related_name='bill_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
