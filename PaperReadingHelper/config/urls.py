from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from config.views import HomeView
from config.views import LoginView, RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('', include('user.urls')),
    
]
