# Generated by Django 2.0.1 on 2018-02-08 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0015_auto_20180208_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='movie_name_id',
        ),
    ]
