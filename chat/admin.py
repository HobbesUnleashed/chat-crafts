from django.utils.html import strip_tags
from django.contrib import admin
from .models import Category
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display = ("plain_title", "plain_description")
    summernote_fields = (
        "title",
        "description",
    )

    def plain_title(self, obj):
        return strip_tags(obj.title)

    def plain_description(self, obj):
        return strip_tags(obj.description)

    plain_title.short_description = "Title"
    plain_description.short_description = "Description"
