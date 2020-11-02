from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('like/', views.like),
    path('dislike/', views.dislike),
    path('comment/', views.comment),
]