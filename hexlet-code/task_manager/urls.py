from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views_box import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', auth.UserListView.as_view(), name='user_list'),
    path('users/create/', auth.UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', auth.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', auth.UserDeleteView.as_view(), name='user_delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='home'),
]
