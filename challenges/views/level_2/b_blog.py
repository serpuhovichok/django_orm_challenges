"""
В этом задании вам предстоит работать с моделью поста в блоге. У него есть название, текст, имя автора, статус
(опубликован/не опубликован/забанен), дата создания, дата публикации, категория (одна из нескольких вариантов).

Ваша задача:
- создать соответствующую модель (в models.py)
- создать и применить миграцию по созданию модели (миграцию нужно добавить в пул-реквест)
- заполнить вашу локальную базу несколькими ноутбуками для облегчения тестирования
- реализовать у модели метод to_json, который будет преобразовывать объект книги в json-сериализуемый словарь
- по очереди реализовать каждую из вьюх в этом файле, проверяя правильность их работу в браузере
"""
import datetime

from django.http import HttpRequest, HttpResponse, JsonResponse
from challenges.models import BlogPost


def last_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть 3 последних опубликованных поста.
    """
    posts = BlogPost.objects.order_by('-publish_date')[:3]
    result = []
    for post in posts:
        result.append(post.to_json())
    return JsonResponse(result, safe=False)


def posts_search_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть все посты, которые подходят под поисковый запрос.
    Сам запрос возьмите из get-параметра query.
    Подходящесть поста можете определять по вхождению запроса в название или текст поста, например.
    """
    query = request.GET['query']
    result = []
    for post in BlogPost.objects.filter(title__contains=query):
        if post.to_json() not in result:
            result.append(post.to_json())
    for post in BlogPost.objects.filter(text__contains=query):
        if post.to_json() not in result:
            result.append(post.to_json())

    return JsonResponse(list(result), safe=False)


def untagged_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть все посты без категории, отсортируйте их по автору и дате создания.
    """
    posts = BlogPost.objects.filter(category__isnull=True).order_by('author', 'create_date')
    result = []
    for post in posts:
        result.append(post.to_json())
    return JsonResponse(result, safe=False)

def categories_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть все посты все посты, категория которых принадлежит одной из указанных.
    Возьмите get-параметр categories, в нём разделённый запятой список выбранных категорий.
    """
    categories = request.GET['categories'].split(',')
    posts = BlogPost.objects.filter(category__in=categories)
    result = []
    for post in posts:
        result.append(post.to_json())
    return JsonResponse(result, safe=False)

def last_days_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть посты, опубликованные за последние last_days дней.
    Значение last_days возьмите из соответствующего get-параметра.
    """
    last_days = int(request.GET['last_days'])
    date_border = datetime.datetime.now().date() - datetime.timedelta(days=last_days)
    posts = BlogPost.objects.filter(publish_date__gte=date_border)
    result = []
    for post in posts:
        result.append(post.to_json())
    return JsonResponse(result, safe=False)