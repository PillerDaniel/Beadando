# Generated by Django 3.2.12 on 2022-12-30 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_post_gumimeret'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=750),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
