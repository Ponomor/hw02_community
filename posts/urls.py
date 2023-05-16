from django.urls import path 
from . import views

urlpatterns = [
    path('group/<slug>/', views.group_posts, name='group_posts'), #, name ='group_posts'
    path('', views.index, name="index"),
    path('new/',views.new_post, name="new"),
    # Профайл пользователя
    path('<str:username>/', views.profile, name='profile'),
    # Просмотр записи
    path('<str:username>/<int:post_id>/', views.post_view, name='post'),
    path(
        '<str:username>/<int:post_id>/edit/', 
        views.post_edit, 
        name='post_edit'
    ),
]
