from django.shortcuts import render
from portfolio.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    post_list = Post.objects.filter(id__gt=1).order_by('-created')
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'posts': posts})


def bio(request):
    # First post is the bio
    ctx = {'post': Post.objects.first()}
    return render(request, 'bio.html', ctx)


def portfolio(request):
    return render(request, 'portfolio.html')
