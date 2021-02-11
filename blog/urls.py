from django.urls import path
from blog.views import (
                        landing_page,
                        index,
                        post_detail,
                        post_like,
                        create_post,
                        post_topic,
                        my_posts,
                        update_post,
                    )

app_name = "blog"

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("home/", index, name="home"),
    path("new/post/", create_post, name="create-post"),
    path("post/<int:pk>/detail/", post_detail, name="post-detail"),
    path("post/<int:pk>/like/", post_like, name="post-like"),
    path("topic/<int:pk>/", post_topic, name="post-topic"),
    path("user/<int:pk>/posts/", my_posts, name="my_posts"),
    path("post/<int:pk>/update", update_post, name="update-post")
]
