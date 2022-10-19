from django.shortcuts import render


def base(request):
    return render(request, 'base.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog_details(request):
    return render(request, 'blog-details.html', {})

def blog_home(request):
    return render(request, 'blog-home.html', {})

def contact_us(request):
    return render(request, 'contact-us.html', {})

def elements(request):
    return render(request, 'elements.html', {})

def index(request):
    return render(request, 'index.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def test(request):
    return render(request, 'test.html', {})
