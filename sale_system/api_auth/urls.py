from django.urls import path

# views
from . import views

urlpatterns = [
    path('users/', views.UserListCreateView.as_view()),
    path('login_token/', views.LoginView.as_view()),
]
