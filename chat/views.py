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
    template_name = "crafts/postlist.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_context_data(self):
        context = super().get_context_data()
        category_id = self.request.resolver_match.kwargs.get(
            "category_id"
        )  # Fetch category_id directly from URL
        context["category"] = get_object_or_404(Category, pk=category_id)
        return context
