from django.shortcuts import get_object_or_404, render
from .models import Group, Post


def index(request):
    template = "posts/index.html"
    title = "Это главная страница проекта Yatube"
    posts = Post.objects.select_related('group')[:10]
    context = {
        "title": title,
        "posts": posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    group_list = "posts/group_list.html"
    title = "Записи сообщества"
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:10]
    context = {
        "title": title,
        "group": group,
        "posts": posts
    }
    return render(request, group_list, context)
