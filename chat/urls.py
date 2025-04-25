from . import views
from django.urls import path
from django.conf import settings
from .views import edit_post
from chat.views import custom_404


urlpatterns = [
    path("", views.Categories.as_view(), name="home"),
    path("create-post/", views.create_post_page, name="create_post_page"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path(
        "category/<int:category_id>/posts/", views.PostList.as_view(), name="posts_list"
    ),
    path(
        "posts/<int:post_id>/edit_comment/<int:comment_id>/",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "posts/<int:post_id>/delete_comment/<int:comment_id>/",
        views.comment_delete,
        name="comment_delete",
    ),
    path("posts/<int:post_id>/delete/", views.delete_post, name="delete_post"),
    path("post/<int:pk>/edit/", edit_post, name="post_edit"),
    path(
        "test-404/",
        lambda request: custom_404(request, Exception("Test")),
        name="test_404",
    ),
]

handler404 = "chat.views.custom_404"
handler500 = "chat.views.custom_500"
