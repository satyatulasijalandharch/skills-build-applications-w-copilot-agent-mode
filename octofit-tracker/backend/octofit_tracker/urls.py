"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.api_root, name='api-root'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<str:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('teams/', views.TeamList.as_view(), name='team-list'),
    path('teams/<str:pk>/', views.TeamDetail.as_view(), name='team-detail'),
    path('activity/', views.ActivityList.as_view(), name='activity-list'),
    path('activity/<str:pk>/', views.ActivityDetail.as_view(), name='activity-detail'),
    path('leaderboard/', views.LeaderboardList.as_view(), name='leaderboard-list'),
    path('leaderboard/<str:pk>/', views.LeaderboardDetail.as_view(), name='leaderboard-detail'),
    path('workouts/', views.WorkoutList.as_view(), name='workout-list'),
    path('workouts/<str:pk>/', views.WorkoutDetail.as_view(), name='workout-detail'),
]
