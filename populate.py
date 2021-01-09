import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bloggy.settings')

import django
django.setup()

from faker import Faker
from django.contrib.auth.models import User
from accounts.models import Profile
from articles.models import Article
from django.db import IntegrityError, ProgrammingError
import random
fake = Faker()

'''
pip install Faker # first
'''


def fake_users(n):
  for i in range(2, n):
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = first_name + last_name
    email = fake.email()
    user = User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    user.save()

    profile = Profile(user=user)
    profile.bio = fake.sentence() + ' ' + fake.sentence() + ' ' + fake.sentence()
    if IntegrityError or ProgrammingError:
      pass
    else:
      profile.save()


def fake_articles(n):
  total_users = User.objects.count()

  for i in range(0, n):
    random_user_index = random.randint(1, total_users - 1)

    user = User.objects.all()[random_user_index]
    # user = User.objects.get(pk=random_user_index)

    title = fake.sentence()
    message = ""

    for j in range(0, 10):
      message += '<p>' + fake.sentence() + '</p>'
      # message += '&nbsp;' * 4 + fake.sentence()
      for lam in range(0, 40):
        message += fake.sentence() + ' '
      # message += '<br><br>'
    # created_date = fake.past_date(
      # start_date="-1y", tzinfo='Europe/Istanbul')
    article = Article(
        user=user,
        title=title,
        message=message,
        # created_date=created_date,
    )
    article.save()

    for i in range(0, 4):
      article.tags.add(fake.color_name())
    article.save()


if __name__ == "__main__":
  fake_users(10)
  fake_articles(100)
