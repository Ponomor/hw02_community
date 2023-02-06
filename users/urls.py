# from django.contrib.auth.views import (
#     LoginView,
#     LogoutView,
#     PasswordResetCompleteView,
#     PasswordResetConfirmView,
#     PasswordResetDoneView,
#     PasswordResetView,
#     PasswordChangeView,
#     PasswordChangeDoneView,

# )
from django.urls import path
from .import views
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    # path('login/', LoginView.as_view(), name = 'login' ),
    # path('logout/', LogoutView.as_view(), name ='logout'),
    # path('password_change/', PasswordChangeView.as_view(), name= 'password_change' ),
    # path('password_change/done/',PasswordChangeDoneView.as_view(),name= 'password_change_done'),
    # path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done', PasswordResetDoneView.as_view(), name='password_reset_confim'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confim'),
    # path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
