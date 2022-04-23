from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('song/', views.index, name='index'),
    path('song/<int:song_id>/', views.detail, name='detail'),
]
