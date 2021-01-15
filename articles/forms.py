from django import forms
from django.core.exceptions import ValidationError
from tinymce.widgets import TinyMCE
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
  class Meta():
    # abstract = True
    model = Article
    fields = ('image', 'title', 'message', 'tags')
    widgets = {
      'title': forms.Textarea(attrs={'placeholder': 'Başlık'}),
      'message': forms.CharField(widget=TinyMCE())
    }

  def title_namecheck(self):
    title = self.cleaned_data.get('title')
    if Article.objects.filter(title=title):
      raise ValidationError('Bu başlığa sahip bir yazı mevcut. Başka bir başlık seçebilirsiniz.')

  def clean_image(self):
    image = self.cleaned_data.get('image', False)
    if image:
      if image._size > 5 * 1024 * 1024:
        raise ValidationError("Yazı görseli çok büyük ( > 5mb )")
      return image
    else:
      raise ValidationError("Yüklenen görsel okunamadı")

  # def __init__(self, *args, **kwargs):
  #   user = kwargs.pop('user', None)
  #   super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    # fields = ('content',) find a way to completly hide article and author on html
    # prolly gonna change
    fields = ('content', 'article', 'author')
    widgets = {'article': forms.HiddenInput(), 'author': forms.HiddenInput()}

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
