# blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post
from .models import Comment
from django import forms

class TagWidget(forms.TextInput):
    pass


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email already in use.")
        return email

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Email already in use.")
        return email

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "avatar"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

        widgets = {
            'tags': TagWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

