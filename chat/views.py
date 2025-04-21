from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView
from .models import Category, Post


# Create your views here.
class Categories(generic.ListView):
    queryset = Category.objects.all()
    template_name = "chat/categories.html"


class PostList(ListView):
    model = Post
    template_name = "chat/postlist.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        """Filters posts by the chosen category"""
        category_id = self.kwargs["category_id"]  # Extract category_id from URL
        category = get_object_or_404(Category, pk=category_id)
        return Post.objects.filter(category=category).order_by("-created_on")

    def get_context_data(self, **kwargs):
        """Adds category data to context"""
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(Category, pk=self.kwargs["category_id"])
        return context
