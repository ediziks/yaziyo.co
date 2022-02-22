from django import template
import readtime
import math

register = template.Library()


def read(html):
  with_text = readtime.of_html(html)
  result = math.ceil(with_text.seconds / 60)
  return result


register.filter('readtime', read)
