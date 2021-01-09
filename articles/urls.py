from django.urls import path, include
from . import views


app_name = 'articles'

urlpatterns = [
  path('new/', views.CreateArticle.as_view(), name='create'),
  path('tags/<str:tag>/', views.TagsListView.as_view(), name='tags'),
  path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
  path('add_bookmark/<str:bookmark_slug>/', views.add_bookmark, name='add_bookmark'),
  path('delete_bookmark/<str:bookmark_slug>/', views.delete_bookmark, name='delete_bookmark'),
  path('<str:username>/<str:slug>/', views.ArticleDetail.as_view(), name='single'),
  path('<str:username>/<str:slug>/delete/', views.DeleteArticle.as_view(), name='delete'),
  path('<str:username>/<str:slug>/like/', views.ArticleLikeRedirect.as_view(), name='article-like'),
]