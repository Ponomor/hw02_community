from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# class Login(CreateView):
#     form_class = CreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'login.html'   

# Create your views here.
