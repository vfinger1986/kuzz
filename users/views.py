from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import  logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .forms import CustomAuthenticationForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, reverse_lazy
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView






class LoginUser(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    redirect_field_name = 'next'

    def get_success_url(self):
        if self.request.POST.get('next', '').strip():
            return self.request.POST.get('next')
        return reverse_lazy('catalog:catalog')


def logout_user(request):
    logout(request)
    return redirect('main:index')

#class LogoutUser(LogoutView):
    #next_page = reverse_lazy('main:index')



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'users/register_done.html'
    extra_context = {'title': 'Регистрация завершена'}
    
    
class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()  
    form_class = ProfileUserForm  
    template_name = 'users/profile.html'  
    extra_context = {'title': 'Профиль пользователя','active_tab': 'profile'} 

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change_form.html'
    extra_context = {'title': 'Изменение пароля',
                     'active_tab': 'password_change'}
    success_url = reverse_lazy('users:password_change_done')
    
    
class UserPasswordChangeDone(TemplateView):
    template_name = 'users/password_change_done.html'
    extra_context = {'title': 'Пароль успешно изменен'}





















# Create your views here.
