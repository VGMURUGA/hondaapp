# Generated by Django 4.1 on 2022-09-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_bike_title_two_wheeler_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='four_wheeler',
            name='url',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AddField(
            model_name='two_wheeler',
            name='url',
            field=models.CharField(default='a', max_length=100),
        ),
    ]
