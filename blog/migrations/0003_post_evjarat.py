# Generated by Django 3.2.12 on 2022-12-30 19:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221230_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='evjarat',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
