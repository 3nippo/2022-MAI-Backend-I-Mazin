from django.urls import path
from . import views

urlpatterns = [
    path('', views.views.index, name='index'),
    path('data/', views.api.account_data, name='account_data'),
    path('data/<int:pk>/', views.api.specific_account_data, name='specific_account_data'),
    path('age_bars/', views.api.age_bars, name='age_bars'),
]
