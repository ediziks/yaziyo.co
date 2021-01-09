from django.views.generic import TemplateView, View, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from articles.models import Article
from django.contrib.auth import get_user_model
from django.shortcuts import render
from el_pagination.decorators import page_template
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.db.models import F
from el_pagination.views import AjaxListView
from django.db.models import Count


class HomePage(TemplateView):
  template_name = 'index.html'


class SearchView(AjaxListView):
  template_name = 'search.html'
  page_template = 'search_page.html'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['query'] = self.request.GET.get('q')
    # if extra_context is not None:
    #   context.update(extra_context)
    return context

  def get_queryset(self):
    query = self.request.GET.get('q')

    if query is not None:
      search_query = SearchQuery(query)
      search_rank = SearchRank(F('search_vector'), search_query)
      results = Article.objects.annotate(rank=search_rank).filter(search_vector=search_query, rank__gte=0.3).order_by('-rank')
      return results


@page_template('index_page.html')
def index(request, template='index.html', extra_context=None):
  context = {
      # 'userlist': User.objects.all()[:10],
      'articlelist': Article.objects.all(),
      'editorpicks': Article.objects.annotate(like_counts=Count('likes')).order_by('-like_counts')[:6],
      'top_tags': Article.tags.most_common()[:10],
  }
  # notifications dropdown is only working on index.html and that's an issue
  if request.user.is_authenticated:
    context['notifications'] = request.user.notifications.all()[:10]
  if extra_context is not None:
    context.update(extra_context)
  return render(request, template, context)


# not working yet
# def notifications_navbar(request):
#   template = 'noti_nav.html'
#   if request.user.is_authenticated:
#     context = {
#       'notifications': request.user.notifications.all()
#     }
#   print('NOTIS CALLEDDDDDDDDDDDDDDDDDDDDDD HERE')
#   return render(request, template, context)
