# Generated by Django 3.1.5 on 2021-03-25 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_auto_20210326_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookservice',
            name='organzition_id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='organzition_id',
        ),
        migrations.AddField(
            model_name='bookservice',
            name='organzition_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bigservice',
            name='dateServics',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smallservice',
            name='dateServics',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Organzition',
        ),
    ]
