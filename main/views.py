from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    main_content = Main.objects.all()
    latest_entries = Entry.objects.order_by('-date')[0:5]
    context = {'main_content': main_content, 'latest_entries': latest_entries}
    return render(request, 'main/index.html', context)

def entries(request):
    entries = Entry.objects.order_by('-date')
    context = {'entries': entries}
    return render(request, 'main/entries.html', context)

def entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    context = {'entry': entry}
    return render(request, 'main/entry.html', context)

def categories(request):
    categories = Category.objects.sort_by('name')
    context = {'categories': categories}
    return render(request, 'main/categories.html', context)

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    entries = category.entry_set.order_by('-date')
    context = {'category': category, 'entries': entries}
    return render(request, 'main/category.html', context)
