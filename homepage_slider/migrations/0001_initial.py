# Generated by Django 5.1.3 on 2024-11-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_heading', models.CharField(max_length=200)),
                ('secondary_heading', models.CharField(max_length=300)),
                ('background_image', models.ImageField(upload_to='slider_images/')),
                ('logo', models.ImageField(upload_to='slider_logos/')),
                ('overlay_text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]