from django.urls import path
from . import views

urlpatterns = [
    path('somewhere/', views.somewhere_view, name='somewhere_view'),
    path('configure/', views.config_view, name='config_view'),
]
