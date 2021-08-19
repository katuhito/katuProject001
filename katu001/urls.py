from django.urls import path
from . import views

app_name = 'katu001'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog-detail/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
    
]