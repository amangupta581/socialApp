from django.urls import path
from .views import *

app_name = "newsfeed"

urlpatterns = [
    path("post/create", CommentSerializer.as_view(), name="post-create"),
]
