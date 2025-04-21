from django.utils.html import strip_tags
from django.contrib import admin
from .models import Category, Post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display = ("plain_title", "plain_description")
    list_filter = ("title",)

    def plain_title(self, obj):
        return strip_tags(obj.title)

    def plain_description(self, obj):
        return strip_tags(obj.description)

    plain_title.short_description = "Title"
    plain_description.short_description = "Description"


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "category", "age", "skill", "created_on")
    search_fields = ["title", "category"]
    list_filter = ("category", "title")
