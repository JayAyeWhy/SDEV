from . import views
from django.urls import path
from .views import home
urlpatterns = [
    path("", views.home, name = "home"),
    path("Login/", views.Login, name='Login'),
    path("Order/", views.Login, name='Order'),
    path("Menu/", views.Menu, name='Menu'),
    path("Admin/", views.Admin, name='Admin'),
    path('register/', views.register_view, name ="register")
]