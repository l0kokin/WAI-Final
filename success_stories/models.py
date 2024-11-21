from django.db import models

class CardContent(models.Model):
    program_name = models.CharField(max_length=255)
    student_full_name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='card_images/')

    def __str__(self):
        return f"{self.student_full_name} - {self.program_name}"


class GraduateSuccess(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    linkedin_url = models.URLField()

    def __str__(self):
        return self.full_name
