"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from adapter.population_records.population_records_controller import PopulationRecordsGrowthOverTimeView
from adapter.traffic_incidents.traffic_incidents_controller import IncidentsOverTimeView
from adapter.users.user_controller import UsersView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/login/", TokenObtainPairView.as_view()),
    path("api/auth/refresh/", TokenRefreshView.as_view()),
    path("api/auth/me/", UsersView.as_view()),
    path(
        "api/population-records/growth-over-time/",
        PopulationRecordsGrowthOverTimeView.as_view(),
    ),
    path(
        "api/traffic-incidents/growth-over-time/",
        IncidentsOverTimeView.as_view(),
    ),
]
