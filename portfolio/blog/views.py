from django.shortcuts import render
from portfolio.blog.models import Entry
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.db.models import Q


def blog(request):
    entry_list = Entry.objects.filter(published=True)
    paginator = Paginator(entry_list, 10)

    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        # If page not an integer, deliver first page
        entries = paginator.page(1)
    except EmptyPage:
        # If no more results, deliver last of results
        entries = paginator.page(paginator.num_pages)

    ctx = {
        'entries': entries,
    }

    return render(request, 'blog/entries.html', ctx)


def entries_with_given_tag(request, tag_name):
    entries = Entry.objects.filter(tags__name=tag_name)

    ctx = {
        'entries': entries
    }

    return render(request, 'blog/entries.html', ctx)


def entry(request, pk):
    entry = get_object_or_404(Entry, id=pk)

    ctx = {
        'entry': entry,
    }

    return render(request, 'blog/entry.html', ctx)


def about(request):
    return render(request, 'blog/about.html')


def portfolio(request):
    return render(request, 'blog/portfolio.html')


def search_results(request, search_string):
    query = None
    for word in search_string.split():
        subquery = Q(title__icontains=word) | Q(body__icontains=word)
        query = (subquery & query) if query else subquery
    entries = Entry.objects.filter(query)

    ctx = {
        'entries': entries
    }
    return render(request, 'blog/entries.html', ctx)


def entry_preview(request, pk):
    entry = get_object_or_404(Entry, id=pk)

    ctx = {
        'entry': entry,
    }

    return render(request, 'blog/entry.html', ctx)


def unpublished_entries(request):

    entry_list = Entry.objects.filter(published=False)
    paginator = Paginator(entry_list, 10)

    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        # If page not an integer, deliver first page
        entries = paginator.page(1)
    except EmptyPage:
        # If no more results, deliver last of results
        entries = paginator.page(paginator.num_pages)

    ctx = {
        'entries': entries,
    }

    return render(request, 'blog/entries.html', ctx)
