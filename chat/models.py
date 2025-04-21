from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to="category-images/", default="category-images/no-image.jpg"
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{ self.title } | { self.description }"
