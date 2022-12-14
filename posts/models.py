from django.db import models
from django.contrib.auth import get_user_model
# from django.shortcuts import reverse

User = get_user_model() 

class Group(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
     
    def __str__(self):
        return self.title 

    # def get_absolute_url(self):
    #     return reverse('myurl', kwargs={'slug': self.slug})


class Post(models.Model):
    text = models.TextField() 
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE, related_name='posts')
    
    def __str__(self):
        return self.text
