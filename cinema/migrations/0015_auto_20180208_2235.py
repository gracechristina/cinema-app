# Generated by Django 2.0.1 on 2018-02-08 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0014_movies_movie_name_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movie_name_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.Cinema'),
        ),
    ]
