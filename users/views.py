from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from posts.forms import NewForm

# def new(request):
#     if request.method == 'POST':
#         form = NewForm(request.POST)
#         return render(request, 'new.html', {'form': form})
#     # form = NewForm()
#     # return render(request, 'new.html', {'form': form})
# # form = ExchangeForm()
# # return render(request, 'index.html', {'form': form})
# # def new_post(text,group):
# #     body = f''' 
# #     Текст: {text}
# #     Група: {group}
# #     '''
#     # post(body)

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# class New(CreateView):
#     form_class = CreationForm
#     success_url = reverse_lazy('new')



# class SignUp(CreateView):
#     # """Собственная форма регистрации пользователя."""

#     form_class = CreationForm
#     success_url = reverse_lazy("posts:index")
#     template_name = "users/signup.html"

# class Login(CreateView):
#     form_class = CreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'login.html'   

# Create your views here.
