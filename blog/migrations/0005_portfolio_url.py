# Generated by Django 4.1.7 on 2023-03-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]