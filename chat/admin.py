from django.utils.html import strip_tags
from django.contrib import admin
from .models import Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display = ("plain_title", "plain_description", "image_preview")
    list_filter = ("title",)

    def plain_title(self, obj):
        return strip_tags(obj.title)

    def plain_description(self, obj):
        return strip_tags(obj.description)

    def image_preview(self, obj):
        return f'<img src="{obj.image.url}" width="75%"/>'

    plain_title.short_description = "Title"
    plain_description.short_description = "Description"
    image_preview.allow_tags = True


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "category", "age", "skill", "created_on")
    search_fields = ["title", "category"]
    list_filter = ("category", "title")


admin.site.register(Comment)
