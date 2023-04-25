"""ideaPlace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ideas import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.home_view, name='home'),
    path('create/', views.idea_create, name='idea_create'),
    path('logout/', views.logout_view, name='logout'),
    path('ideas/create/', views.idea_create, name='idea_create'),
    path('ideas/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('ideas/<int:pk>/update/', views.idea_update, name='idea_update'),
    path('ideas/<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('user/', views.user_profile, name='user_profile'),
    path('user/ideas/', views.user_ideas, name='user_ideas'),
    path('like/<int:pk>/', views.idea_like, name='idea_like'),
    path('search/', views.idea_search, name='idea_search'),


]
