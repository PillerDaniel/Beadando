# Generated by Django 3.2.12 on 2022-12-30 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20221230_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='kobcenti',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='uzemanyag',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
