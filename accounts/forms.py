from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .models import Profile


class SignUpForm(UserCreationForm):
  captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', 'captcha')

  def clean(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
      raise ValidationError('Bu mail adresi zaten kayıtlı!')
    return self.cleaned_data


class LoginForm(AuthenticationForm):
  captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

  class Meta:
    model = User
    fields = ('username', 'email', 'captcha')


class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['avatar', 'cover', 'bio']
