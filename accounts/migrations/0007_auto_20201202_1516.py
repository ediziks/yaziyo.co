# Generated by Django 3.0.7 on 2020-12-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201202_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover',
            field=models.ImageField(default='default_coverr.jpg', upload_to='covers/'),
        ),
    ]
