from django.db import models


class LiteracyCard(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField()
    link = models.URLField()

    def __str__(self):
        return self.title
