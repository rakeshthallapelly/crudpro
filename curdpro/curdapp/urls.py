from django.urls import path

from . import views

urlpatterns = [
    path('', views.Create.as_view()),
    path('<int:pk>/', views.Retrive.as_view()),
]