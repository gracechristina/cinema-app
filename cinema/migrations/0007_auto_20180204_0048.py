# Generated by Django 2.0.1 on 2018-02-03 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0006_cinema'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinema',
            old_name='cinema',
            new_name='name',
        ),
    ]
