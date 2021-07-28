from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_exam, name="create_exam"),
    path('read/<slug:slug>/', views.read_exam, name="read_exam"),
    path('update/<slug:slug>/', views.update_exam, name="update_exam"),
]