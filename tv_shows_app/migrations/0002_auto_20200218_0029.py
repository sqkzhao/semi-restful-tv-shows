# Generated by Django 2.2 on 2020-02-18 00:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tvshow',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
