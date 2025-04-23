from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import ListView
from .models import Category, Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.contrib import messages


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


def post_detail(request, post_id):
    """
    Display an individual :model: `blog.post`

    **Context**

    ``post``
        An instance of :model: `blog.post`.

    **Template:**

    :template: `blog/post_detail.html`
    """

    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )

    comment_form = CommentForm()

    print("About to run the render")

    return render(
        request,
        "chat/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


@login_required
def create_post_page(request):
    if request.method == "POST":
        print("POST request received")
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print("form is valid")
            post = form.save(commit=False)
            print(f"Category from form: {post.category}")  # Debug print
            post.author = request.user
            if post.category is None:
                print("No category assigned!")
            else:
                print(f"Category ID: {post.category.id}")
            post.save()
            print(f"Post saved successfully: {post.title}")
            return redirect("posts_list", category_id=post.category.id)
            print(f"redirecting to posts_list with the category id: {post.category.id}")
        else:
            print("form is invalid")
            print(form.errors)
    else:
        form = PostForm()

    return render(request, "chat/create_post.html", {"form": form})
