from django.db import models


class Program(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=500)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.title


class LiteracyCard(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='literacy_images/')
    link = models.URLField()

    def __str__(self):
        return self.title
