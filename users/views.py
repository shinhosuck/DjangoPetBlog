from django.shortcuts import render, redirect
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ContactUsForm
from django.contrib import messages
from django.contrib.auth.models import User

def user_register(request):
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, f"{request.user.username} has successfully registered.")
            return redirect("users:login")
    else:
        register_form = UserRegisterForm()
    return render(request, "users/register.html", {"register_form": register_form})

def profile(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if  u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "{}'s profile has been updated!".format(request.user))
            return redirect("users:profile")
        else:
            messages.success(request, """Your profile failed to update! Try agin.
                Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.""")
            return redirect("users:profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, "users/profile.html", context)


def contact_us_forms(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, f"Thank you very much for the message. I will get back to you as soon as possible.")
        return redirect("blog:home")
    else:
         messages.warning(request, f"Message did not sent. Please try again!")
    return redirect("blog:home")