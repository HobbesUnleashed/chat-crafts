from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = CloudinaryField("image", default="no_image_fvpesk")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title


class Post(models.Model):
    AGE = (
        (0, "5+"),
        (1, "8+"),
        (2, "10+"),
        (3, "13+"),
        (4, "15+"),
        (5, "18+"),
    )

    SKILL = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
    )

    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    media_url = models.URLField(
        max_length=250,
        blank=True,
        null=True,
        help_text="Link to your Youtube/Facebook, etc",
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="cat_id"
    )
    materials = models.TextField()
    time_taken = models.IntegerField(help_text="Time taken in minutes")
    age = models.IntegerField(choices=AGE, default=0)
    image = CloudinaryField("image", default="no_image_fvpesk")
    skill = models.IntegerField(choices=SKILL, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="craft_posts"
    )
    blurb = models.CharField(
        max_length=80, unique=False, default="A piece of crafting excellence"
    )
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def get_media_url_as_hyperlink(self):
        if self.media_url:
            return format_html(
                '<a href="{}" target="_blank">{}</a>', self.media_url, self.media_url
            )
        return "No Media URL was provided"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.body} | Written by {self.author}"
