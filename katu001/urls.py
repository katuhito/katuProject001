from django.urls import path
from . import views

app_name = 'katu001'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]