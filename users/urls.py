from . views import user_register, profile, contact_us_forms
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path 



app_name = "users"




urlpatterns = [
    path("register/", user_register, name="register"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("user/profile/", profile, name="profile"),
    path("contact_us/", contact_us_forms, name="contact_us"),
]