# Generated by Django 4.1 on 2022-09-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_rename_url_four_wheeler_carurl_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='four_wheeler',
            name='status',
        ),
        migrations.RemoveField(
            model_name='two_wheeler',
            name='status',
        ),
        migrations.AddField(
            model_name='four_wheeler',
            name='Available',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='four_wheeler',
            name='Booked',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='four_wheeler',
            name='Totalstock',
            field=models.IntegerField(default=5, max_length=100),
        ),
        migrations.AddField(
            model_name='two_wheeler',
            name='Available',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='two_wheeler',
            name='Booked',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='two_wheeler',
            name='Totalstock',
            field=models.IntegerField(default=5, max_length=100),
        ),
    ]
