from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from rest_framework.reverse import reverse_lazy

from users.forms import UserRegisterForm, UserLoginForm


class UserRegisterView(CreateView):
    model = get_user_model()
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class UserLoginView(LoginView):
    model = get_user_model()
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:profile')


class UserProfileView(DetailView):
    model = get_user_model()
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset = None):
        return self.request.user




