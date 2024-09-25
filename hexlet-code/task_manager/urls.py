from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views_box import auth
from .views_box.status import (StatusListView,
                               StatusCreateView,
                               StatusUpdateView,
                               StatusDeleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', auth.UserListView.as_view(), name='user_list'),
    path('users/create/', auth.UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', auth.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', auth.UserDeleteView.as_view(), name='user_delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='home'),

    path('statuses/', StatusListView.as_view(), name='status_list'),
    path('statuses/create/', StatusCreateView.as_view(), name='status_create'),
    path('statuses/<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('statuses/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
]
