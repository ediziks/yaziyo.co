# Generated by Django 3.0.7 on 2020-12-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201130_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover',
            field=models.ImageField(default='default_cover.jpg', upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default_avatar.jpg', upload_to='avatars/'),
        ),
    ]
