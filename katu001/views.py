from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import BlogPost

class IndexView(ListView):
    template_name = 'index.html'
    #object_listキーの別名を設定
    context_object_name = 'orderby_records'
    #モデルBlogPostのレコードのオブジェクトにorder_by()を適用して
    #BlogPostのレコードを投稿日時の降順で並べ替える。
    queryset = BlogPost.objects.order_by('-posted_at')
    #1ページに表示するレコードの件数(ページネーション)
    paginate_by = 2

class BlogDetail(DetailView):
    template_name = 'post.html'
    #クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    


    

