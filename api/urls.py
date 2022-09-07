from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('notes/', views.getNotes, name='getNotes'),
    path('notes/create/', views.createNote, name='createNote'),
    path('notes/<str:pk>/', views.getNote, name='getNote'),
    path('notes/<str:pk>/update/', views.updateNote, name='updateNote'),
    path('notes/<str:pk>/delete/', views.deleteNote, name='deleteNote'),
]

