# Generated by Django 3.2.12 on 2022-12-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20221230_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hajtas',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='muszaki',
            field=models.CharField(default=0, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='okmanyok',
            field=models.CharField(default=0, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='sebessegvalto',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]