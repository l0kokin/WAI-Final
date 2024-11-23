from django.db import models


class FaqAilab(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
