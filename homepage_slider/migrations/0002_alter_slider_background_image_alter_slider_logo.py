# Generated by Django 5.1.3 on 2024-11-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage_slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='background_image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='slider',
            name='logo',
            field=models.URLField(),
        ),
    ]
