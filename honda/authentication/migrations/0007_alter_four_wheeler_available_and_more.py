# Generated by Django 4.1 on 2022-09-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_remove_four_wheeler_status_remove_two_wheeler_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='four_wheeler',
            name='Available',
            field=models.IntegerField(default=models.IntegerField(default=5, max_length=100), max_length=100),
        ),
        migrations.AlterField(
            model_name='two_wheeler',
            name='Available',
            field=models.IntegerField(default=models.IntegerField(default=5, max_length=100), max_length=100),
        ),
    ]
