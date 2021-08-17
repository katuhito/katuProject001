from django.db import models
from django.utils import timezone

class BlogPost(models.Model):

    CATEGORY = (('science', '科学のこと'), ('dailytime', '日常のこと'), ('music', '音楽のこと'))

    #タイトル用のフィールド
    title = models.CharField(
        verbose_name = 'タイトル', 
        max_length = 200
    )
    #本文用のフィールド
    content = models.TextField(
        verbose_name = '本文',
    )
    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name = '投稿日時',
        default = timezone.now
    )
    #カテゴリのフィールド
    category = models.CharField(
        verbose_name = 'カテゴリ',
        max_length = 50,
        choices = CATEGORY
    )

    def __str__(self):
        """オブジェクトを文字列に変換して返す
        Returns(str):投稿記事のタイトル
        """
        return self.title




