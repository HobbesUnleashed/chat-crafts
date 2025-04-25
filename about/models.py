from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class ApproachRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Approach request from {self.name}"
