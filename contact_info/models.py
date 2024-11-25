from django.db import models

class ContactInfo(models.Model):
    working_hours = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    transport_info = models.TextField()

    def __str__(self):
        return f"Contact Information"