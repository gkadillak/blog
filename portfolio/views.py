from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from portfolio.models import Post


def home(request):
    post_list = Post.objects.filter(id__gt=1, published=True).order_by('-created')
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'portfolio/home.html', {'posts': posts})


def bio(request):
    # First post is the bio
    ctx = {'post': Post.objects.first()}
    return render(request, 'portfolio/bio.html', ctx)


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def post(request, slug):
    ctx = {'post': Post.objects.get(slug=slug)}
    return render(request, "portfolio/post.html", ctx)
