from django.urls import path
from . import views

urlpatterns = [
    path('', views.views.index, name='index'),
    path('data/', views.api.account_data, name='account_data'),
]
