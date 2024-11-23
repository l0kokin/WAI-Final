from django.db import models


class Slider(models.Model):
    main_heading = models.CharField(max_length=200)
    secondary_heading = models.CharField(max_length=300)
    background_image = models.URLField()
    logo = models.URLField()
    overlay_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.main_heading
