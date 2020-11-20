from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

# posts = [
#     {
#         'author': 'David C',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'November 19 2020'
#     },
#     {
#         'author': 'Shane C',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'November 20 2020'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
