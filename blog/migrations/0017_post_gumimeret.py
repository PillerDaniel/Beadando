# Generated by Django 3.2.12 on 2022-12-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20221230_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gumimeret',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
