# -*- coding: utf-8 -*-
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    context = {
        'title':'django-ecommence',
    }
    return render(request, "core/index.html", context)

def contact(request):

    context = {
    }
    return render(request, "core/contact.html")

def product(request):

    context = {

    }
    return render(request, "core/product.html")

def product_list(request):

    context = {
    }
    return render(request, "core/product_list.html")
