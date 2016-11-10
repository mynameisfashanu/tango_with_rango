from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    return render(request,'rango/index.html',{'categories' : category_list })


def show_category(request, category_name_url):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_url)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request,'rango/category.html',context_dict)


def about(request):
    return render(request,'rango/about.html',{'message' : 'We love you!'})
