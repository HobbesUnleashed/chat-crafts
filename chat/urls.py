from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.Categories.as_view(), name="home"),
    path("posts/<int:category_id>/", views.PostList.as_view(), name="posts_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
