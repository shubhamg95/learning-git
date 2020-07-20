from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.CustomerView.as_view(), name='list'),
    path('create/', views.CustomerView.as_view(), name='create'),
    path('save_customer/', views.CustomerView.as_view(), name='save_customer'),
]