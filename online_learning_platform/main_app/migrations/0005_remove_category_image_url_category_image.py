# Generated by Django 5.0.6 on 2024-05-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_category_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image_url',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='images/default-image.jpg', upload_to='images/'),
        ),
    ]
