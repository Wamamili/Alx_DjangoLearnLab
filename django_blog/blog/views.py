from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm


def home(request):
    return render(request, 'blog/home.html')

class BlogLoginView(LoginView):
    template_name = "blog/auth/login.html"

class BlogLogoutView(LogoutView):
    template_name = "blog/auth/logout.html"

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.strip()
            user.email = form.cleaned_data["email"].strip()
            user.save()
            login(request, user)
            messages.success(request, "Welcome aboard.")
            return redirect("profile")
        messages.error(request, "Fix the errors below.")
    else:
        form = RegistrationForm()
    return render(request, "blog/auth/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "blog/profile.html")

@login_required
def profile_edit(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        messages.error(request, "Fix the errors below.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "blog/profile_edit.html", context)
