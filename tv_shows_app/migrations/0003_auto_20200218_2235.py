# Generated by Django 2.2 on 2020-02-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0002_auto_20200218_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='desc',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='release_date',
            field=models.DateField(),
        ),
    ]
