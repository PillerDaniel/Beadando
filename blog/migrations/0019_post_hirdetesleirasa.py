# Generated by Django 3.2.12 on 2022-12-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20221230_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hirdetesleirasa',
            field=models.TextField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]