from django.contrib import admin
from .models import About, ApproachRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)


@admin.register(ApproachRequest)
class ApproachAdmin(admin.ModelAdmin):

    list_display = ("message", "read")
