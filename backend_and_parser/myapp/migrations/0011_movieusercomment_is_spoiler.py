# Generated by Django 2.2.11 on 2020-11-07 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_movieusercomment_is_spoiler'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieusercomment',
            name='is_spoiler',
            field=models.BooleanField(default=False),
        ),
    ]