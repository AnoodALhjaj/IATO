# Generated by Django 3.1.5 on 2021-03-25 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_auto_20210326_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookservice',
            name='organzition_name',
        ),
        migrations.AddField(
            model_name='customerbill',
            name='organzition_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]