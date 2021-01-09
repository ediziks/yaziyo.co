from django.contrib import admin
from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title', 'pk', 'user', 'created_date')
  search_fields = ('user__username', 'pk', 'title')


class CommentAdmin(admin.ModelAdmin):
  list_display = ('article', 'pk', 'author', 'created_date')
  search_fields = ('article__title', 'pk', 'author__username')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
