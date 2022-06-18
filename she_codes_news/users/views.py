# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

# Added a view for creating a new account
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url= reverse_lazy('login')
    template_name= 'users/createAccount.html'

# Added a view for user profile
class UserView(generic.DetailView):
    model = CustomUser
    template_name = 'users/userProfile.html'
    context_object_name = 'user'




