from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views import generic
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model
from taggit.models import Tag
from . import models, forms
from accounts.models import Profile
from notifications.signals import notify


class CreateArticle(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
  fields = ('image', 'title', 'message', 'tags')
  model = models.Article

  def form_valid(self, form):
    if form.is_valid():
      self.object = form.save(commit=False)
      self.object.user = self.request.user
      self.object.save()
      # the next line is for tags
      form.save_m2m()
      return super().form_valid(form)

  def get_success_url(self):
    return reverse('articles:single', kwargs={'username': self.object.user.username, 'slug': self.object.slug})


class DeleteArticle(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
  model = models.Article
  select_related = ('user',)
  template_name = 'articles/article_confirm_delete.html'

  def get_queryset(self):
    queryset = super().get_queryset()
    return queryset.filter(user_id=self.request.user.pk, slug=self.kwargs['slug'])

  def delete(self, *args, **kwargs):
    # messages.success(self.request, 'Article Deleted')
    return super().delete(*args, **kwargs)

  def get_success_url(self, **kwargs):
    if kwargs != None:
      return reverse_lazy('accounts:profile', kwargs={'username': self.request.user})
    else:
      return reverse_lazy('home')


class ArticleDetail(SelectRelatedMixin, FormMixin, generic.DetailView):
  model = models.Article
  select_related = ('user',)
  form_class = forms.CommentForm

  def get_success_url(self):
    return reverse('articles:single', kwargs={'username': self.object.user.username, 'slug': self.object.slug})

  def get_queryset(self):
    queryset = super().get_queryset().filter(user__username__iexact=self.kwargs.get('username'))
    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['form'] = forms.CommentForm(initial={'article': self.object, 'author': self.request.user})
    return context

  # post comment
  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    form = self.get_form()
    if form.is_valid():
      if request.user != self.object.user:
        notify.send(request.user, recipient=self.object.user, action_object=self.object, verb='yorum')
      return self.form_valid(form)
    else:
      return self.form_invalid(form)

  def form_valid(self, form):
    if form.is_valid():
      form.save()
      return super(ArticleDetail, self).form_valid(form)


@login_required
def delete_comment(request, pk):
  comment = get_object_or_404(models.Comment, pk=pk)
  article_username = comment.article.user.username
  article_slug = comment.article.slug
  comment.delete()
  return redirect('articles:single', username=article_username, slug=article_slug)


class ArticleLikeRedirect(generic.RedirectView):
  def get_redirect_url(self, *args, **kwargs):
    username = self.kwargs.get('user__username')
    slug = self.kwargs.get('slug')
    obj = get_object_or_404(models.Article, slug=slug)
    act_obj = models.Article.objects.get(slug=slug)
    url_ = obj.get_absolute_url()
    user = self.request.user
    if user.is_authenticated:
      if user in obj.likes.all():
        obj.likes.remove(user)
      else:
        obj.likes.add(user)
        if user != obj.user:
          notify.send(user, recipient=obj.user, action_object=act_obj, verb='like')
    return url_


class TagsListView(generic.ListView):
  template_name = 'articles/article_tags.html'
  context_object_name = 'tags_list'

  def get_queryset(self):
    return models.Article.objects.filter(tags__slug__in=[self.kwargs['tag']])

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['tag'] = self.kwargs['tag']
    return context


@login_required
def add_bookmark(request, bookmark_slug):
  user_profile = Profile.objects.get(user=request.user)
  article = models.Article.objects.get(slug=bookmark_slug)
  user_profile.bookmarks.add(article)
  return redirect('accounts:bookmarks', username=request.user.username)


def delete_bookmark(request, bookmark_slug):
  user_profile = Profile.objects.get(user=request.user)
  article = article = models.Article.objects.get(slug=bookmark_slug)
  user_profile.bookmarks.remove(article)
  return redirect('accounts:bookmarks', username=request.user.username)
