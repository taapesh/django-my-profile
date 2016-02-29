from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})

def blog(request):
    return render(request, "blog.html", {})

def about(request):
    return render(request, "about.html", {})

def projects(request):
    return render(request, "projects.html", {})

def learn(request):
    return render(request, "learn.html", {})
    