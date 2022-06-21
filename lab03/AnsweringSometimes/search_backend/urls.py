from django.urls import path
from . import views

urlpatterns = [
    path('top_searched/<int:n>/', views.api.top_n_searched, name='top_n_searched'),
    path('top_marketing/<int:n>/', views.api.top_n_marketed, name='top_n_marketed'),
]
