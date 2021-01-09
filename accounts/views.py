from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, View, DetailView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db import IntegrityError
# from django.http import HttpResponse
# from django.http import Http404
from braces.views import SelectRelatedMixin
from django.views.generic.detail import BaseDetailView
from django.contrib.auth import get_user_model
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from articles.models import Article
from django.contrib import messages
# from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from el_pagination.views import AjaxListView
from notifications.signals import notify
from django.views.generic.edit import FormMixin
from django.conf import settings
import requests

user = get_user_model()


def signup_view(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      #   ''' Begin reCAPTCHA validation '''
      #   recaptcha_response = request.POST.get('g-recaptcha-response')
      #   data = {
      #       'secret': settings.RECAPTCHA_PRIVATE_KEY,
      #       'response': recaptcha_response
      #   }
      #   r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
      #   result = r.json()
      #   print(result)
      #   ''' End reCAPTCHA validation '''
      #   if result['success']:
      user = form.save()
      user.refresh_from_db()
      user.profile.email = form.cleaned_data.get('email')
      user.save()
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=user.username, password=raw_password)
      login(request, user)
      return redirect('home')
  else:
    form = SignUpForm()
  return render(request, 'accounts/signup.html', {'form': form})


# needs pagination
class UserProfileView(SelectRelatedMixin, BaseDetailView, TemplateView, FormMixin):
  model = Profile
  template_name = 'accounts/profile.html'
  select_related = ('user',)

  def get_object(self):
    return self.get_queryset().get(user__username=self.kwargs['username'])

  def get_context_data(self, **kwargs):
    # context = super().get_context_data(**kwargs)
    context = {}
    context['user'] = self.object.user
    # 10 will be changed after pagination
    context['articles'] = Article.objects.filter(user__username=self.object.user.username)[:10]
    return context


@login_required
def profile_update(request, username):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, 'Profil başarıyla güncellendi!')
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

  context = {
    'u_form': u_form,
    'p_form': p_form,
  }

  return render(request, 'accounts/profile_update.html', context)


class ProfileFollowToggle(LoginRequiredMixin, View):
  def post(self, request, *args, **kwargs):
    user_to_toggle = request.POST.get('username')
    profile_ = Profile.objects.get(user__username__iexact=user_to_toggle)
    user = request.user
    if user in profile_.followers.all():
      profile_.followers.remove(user)
    else:
      profile_.followers.add(user)
      notify.send(user, recipient=profile_.user, verb='takip')
    return redirect('accounts:profile', username=user_to_toggle)


class UserNotificationsView(LoginRequiredMixin, ListView):
  context_object_name = 'notifications'
  template_name = 'accounts/notifications.html'

  def get_queryset(self):
    self.request.user.notifications.mark_all_as_read()
    return self.request.user.notifications.all()


class UserBookmarksView(LoginRequiredMixin, ListView):
  context_object_name = 'bookmarks'
  template_name = 'accounts/bookmarks.html'

  def get_queryset(self):
    return self.request.user.profile.bookmarks.all()
