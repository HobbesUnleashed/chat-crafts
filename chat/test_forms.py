import os
from django.test import TestCase
from .forms import CommentForm, PostForm
from .models import Category
import json


class TestCommentForm(TestCase):

    def test_commentform_is_valid(self):
        comment_form = CommentForm({"body": "This is a great post"})
        self.assertTrue(comment_form.is_valid(), msg="CommentForm is not valid")

    def test_commentform_is_invalid(self):
        comment_form = CommentForm({"body": ""})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")


class TestPostForm(TestCase):

    def setUp(self):
        json_path = os.path.join(
            os.path.dirname(__file__), "fixtures", "test_categories.json"
        )
        with open(json_path, "r") as file:
            categories = json.load(file)
            for category in categories:
                Category.objects.create(
                    title=category["title"],
                    description=category["description"],
                    image=category.get("image", "no_image_fvpesk"),
                )

    def test_postform_is_valid(self):
        valid_category = Category.objects.first()
        post_form = PostForm(
            {
                "title": "automated title",
                "category": valid_category.id,
                "content": "automated test content",
                "materials": "Automated materials test",
                "time_taken": "15",
                "age": 3,
                "media_url": "https://www.facebook.com",
                "skill": 3,
            }
        )
        print(post_form.errors)
        self.assertTrue(post_form.is_valid(), msg="PostForm is not valid")

    def test_postform_is_invalid(self):
        valid_category = Category.objects.first()
        post_form = PostForm(
            {
                "title": "",
                "category": None,
                "content": "automated test content",
                "materials": "Automated materials test",
                "time_taken": "not_a_number",
                "age": 6,
                "media_url": "https://www.facebook.com",
                "skill": 999,
            }
        )
        print(post_form.errors)
        self.assertFalse(post_form.is_valid(), msg="Form is valid")
