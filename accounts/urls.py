from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm


app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup_view, name='signup'),
  path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('user/<str:username>/', views.UserProfileView.as_view(), name='profile'),
  path('user/<str:username>/follow/', views.ProfileFollowToggle.as_view(), name='follow'),
  path('user/<str:username>/bookmarks/', views.UserBookmarksView.as_view(), name='bookmarks'),
  path('user/<str:username>/notifications/', views.UserNotificationsView.as_view(), name='notifications'),
  # path('<str:username>/followers/', views.list_followers, name='followers'),
  # path('<str:username>/following/', views.list_following, name='following'),
  path('user/<str:username>/update/', views.profile_update, name='profile_update'),
  path('pass/password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
  path('pass/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
  path('pass/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
  path('pass/password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
