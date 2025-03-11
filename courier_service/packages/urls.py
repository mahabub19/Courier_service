from django.urls import path
from . import views

urlpatterns = [
    path('packages/', views.package_list, name='package-list'),
    path('packages/<int:pk>/', views.package_detail, name='package-detail'),
]