# Generated by Django 4.1.7 on 2023-03-12 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_portfolio_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='image',
            field=models.ImageField(default='admins/default-admin.jpg', upload_to='admins/'),
        ),
    ]
