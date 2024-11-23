from django.db import models


class ResearchArticle(models.Model):
    title = models.CharField(max_length=255)  # Required field
    url = models.URLField()  # Required field
    author = models.CharField(
        max_length=255, blank=True, null=True)  # Optional field

    def __str__(self):
        return self.title
