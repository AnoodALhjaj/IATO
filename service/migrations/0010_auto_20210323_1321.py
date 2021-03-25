# Generated by Django 3.1.5 on 2021-03-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_auto_20210320_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
