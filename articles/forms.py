from django import forms
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
