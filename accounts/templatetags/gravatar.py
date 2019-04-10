import hashlib
# 템플릿 가져오기
from django import template
from django.template.defaultfilters import stringfilter

# 템플릿 라이브러리 가져오기
register = template.Library()

# 필터로 makehash 함수를 추가하기
@register.filter
@stringfilter
def makehash(email):
    return hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
