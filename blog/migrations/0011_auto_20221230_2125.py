# Generated by Django 3.2.12 on 2022-12-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_ajtok'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='karpit',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='sajattomeg',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='teljestomeg',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]