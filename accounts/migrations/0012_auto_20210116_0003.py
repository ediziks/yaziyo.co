# Generated by Django 3.1.5 on 2021-01-15 21:03

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover',
            field=models.ImageField(default='default_cover.jpg', upload_to=accounts.models.cover_upload_dir),
        ),
    ]
