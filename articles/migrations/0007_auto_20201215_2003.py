# Generated by Django 3.1.3 on 2020-12-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default_article_image.jpg', upload_to='article_image/'),
        ),
    ]
