from django.urls import path 
from . views import (
    post_list_view,
)
from . user_auth_view import (
    user_register_view,
    retrieve_token_view,
    user_update_profile_view,
    user_detail_view,
    get_users_view
)

app_name = 'blog_api'


urlpatterns = [
    path('posts/', post_list_view, name='post_api_list'),
    path('register/', user_register_view, name='api-register'),
    path('login/', retrieve_token_view, name='retrieve-token'),
    path('user/<int:id>/update/profile/', user_update_profile_view, name='update-profile'),
    path('user/<int:id>/detail/', user_detail_view, name='user-detail'),
    path('users/', get_users_view, name='users')
]