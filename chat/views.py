from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView
from .models import Category


# Create your views here.
class Categories(generic.ListView):
    queryset = Category.objects.all()
    template_name = "chat/categories.html"
