# Generated by Django 3.2.12 on 2022-12-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_kmora'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='szemelyek',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='kmora',
            field=models.IntegerField(),
        ),
    ]
