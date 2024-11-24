from django.db import models


class FaqAside(models.Model):
    title = models.CharField(max_length=255)
    img_url = models.URLField()
    link_url = models.URLField()
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.title
