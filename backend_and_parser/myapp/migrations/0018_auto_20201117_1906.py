# Generated by Django 2.2.11 on 2020-11-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20201117_1859'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='movieusercomment',
            index=models.Index(fields=['movie', 'score'], name='myapp_movie_movie_i_381e37_idx'),
        ),
    ]
