from django.urls import path

from poll import views

urlpatterns = [


    path('load_form/', views.load_form),
    path('show/', views.show),
    path('edit/<int:id>/', views.edit),






]