from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    content = models.TextField()
    organization = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.organization}"