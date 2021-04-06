from django.urls import path

from bridge import views

urlpatterns = [
    path('', views.home)
]