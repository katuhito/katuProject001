from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages


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
    
class ScienceView(ListView):
    template_name = 'science_list.html'
    #クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'science_records'
    #categry='scienceのレコードを抽出して投稿日時の降順で並べる'
    queryset = BlogPost.objects.filter(category='science').order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 2

class DailylifeView(ListView):
    template_name = 'dailylife_list.html'
    #クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'dailylife_records'
    #categry='scienceのレコードを抽出して投稿日時の降順で並べる'
    queryset = BlogPost.objects.filter(category='dailylife').order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 2

class MusicView(ListView):
    template_name = 'music_list.html'
    #クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'music_records'
    #categry='scienceのレコードを抽出して投稿日時の降順で並べる'
    queryset = BlogPost.objects.filter(category='music').order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 2

class ContactView(FormView):
    """問い合わせページを一覧表示するビュー"""
    template_name = 'contact.html'
    #クラス変数form_classにforms.pyで定義したContactFormを設定
    form_class = ContactForm
    #送信後にリダイレクトするページ
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        """FormViewクラスのForm_valid()をオーバーライド
        フォームのバリデーションを通過したデータがPOSTされたときに呼ばれる
        メール送信を行う
        """
        #forms.pyのsend_email()を実行してメール送信を行う
        form.send_email()
        #送信完了後に表示するメッセージ
        messages.success(self.request, 'お問い合わせは正常に送信されました。')
        #戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)
        



