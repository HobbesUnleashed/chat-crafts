from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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
]
