# Generated by Django 4.1.7 on 2023-03-12 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_customuser_followers_customuser_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
    ]
