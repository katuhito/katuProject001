from django.urls import path
from . import views

app_name = 'katu001'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    #リクエストされたURLが「blog-detail/レコードのid/」の場合にはBlogDetailを実行
    path('blog-detail/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),

    #scienceカテゴリ一覧のURLパターン
    path('science-list/', views.ScienceView.as_view(), name='science_list'),
    #dailylifeカテゴリ一覧のURLパターン
    path('dailylife-list/', views.DailylifeView.as_view(), name='dailylife_list'),
    #musicカテゴリーの一覧のURLパターン
    path('music-list/', views.MusicView.as_view(), name='music_list'), 
    #問い合わせページのURLパターン
    path('contact/', views.ContactView.as_view(), name='contact'),   
]