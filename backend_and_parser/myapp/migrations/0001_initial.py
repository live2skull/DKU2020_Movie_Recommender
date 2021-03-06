# Generated by Django 2.2.11 on 2020-10-13 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('opened_at', models.DateField(null=True)),
                ('genre', models.CharField(max_length=100, null=True)),
                ('img_url', models.CharField(max_length=256, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieUser',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('body', models.TextField(null=True)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user', to='myapp.Movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user', to='myapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='MovieUserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('body', models.TextField(null=True)),
                ('movie_id', models.ForeignKey(on_delete=1, related_name='comments_movieuser', to='myapp.Movie')),
                ('movie_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_movieuser', to='myapp.MovieUser')),
            ],
        ),
    ]
