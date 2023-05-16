# from django.views import Post
from django import forms
from django.forms import ModelForm
from . import models



class NewForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ['text', 'group']

# class PostForm(ModelForm):
#     class Meta:


    # def clean_post(self):
    #     post = self.cleaned_data['post']
    #     if not post.objects.filter(post=post).exists():
    #         raise forms.ValidationError(
    #             'нужен пост',
    #             # params={'artist' : artist},
    #         )
        
    #     return    
