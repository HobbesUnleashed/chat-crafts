from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Category, Post, Comment
from .forms import PostForm, CommentForm


# Categories List View
class Categories(ListView):
    model = Category
    template_name = "chat/categories.html"
    context_object_name = "categories"


# Post List View (Filtered by Category)
class PostList(ListView):
    model = Post
    template_name = "chat/postlist.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        """Filters posts by the chosen category."""
        category_id = self.kwargs.get("category_id")
        category = get_object_or_404(Category, pk=category_id)
        return Post.objects.filter(category=category).order_by("-created_on")

    def get_context_data(self, **kwargs):
        """Adds category data to context."""
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(
            Category, pk=self.kwargs.get("category_id")
        )
        return context


# Post Detail View
def post_detail(request, post_id):
    """Display an individual post and its comments."""
    post = get_object_or_404(Post, pk=post_id)

    # Combine approved comments for all users and unapproved comments for the logged-in user
    if request.user.is_authenticated:
        comments = post.comments.filter(approved=True) | post.comments.filter(
            author=request.user, approved=False
        )
    else:
        comments = post.comments.filter(approved=True)

    # Ensure the comments are ordered by created date
    comments = comments.order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Comment submitted and awaiting approval!")
            return HttpResponseRedirect(reverse("post_detail", args=[post_id]))
        else:
            messages.error(request, "Error submitting comment.")
    else:
        comment_form = CommentForm()

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


# Create New Post View
@login_required
def create_post_page(request):
    """View to create a new post."""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, f"Post '{post.title}' created successfully!")
            return redirect("posts_list", category_id=post.category.id)
        else:
            messages.error(request, "Error creating post. Please check the form.")
    else:
        form = PostForm()

    return render(request, "chat/create_post.html", {"form": form})


def comment_edit(request, post_id, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        post = get_object_or_404(
            Post, pk=post_id
        )  # Fetch the post associated with the comment
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False  # Re-mark as needing approval
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("post_detail", args=[post_id]))


def comment_delete(request, post_id, comment_id):
    """
    view to delete comment
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("post_detail", args=[post_id]))
