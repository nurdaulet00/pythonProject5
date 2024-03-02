from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

def about(request):
    return render(request, 'main/about.html')

def end(request):
    return render(request, 'main/end.html')

def page(request):
    return render(request, 'main/page.html')

def layout(request):
    return render(request, 'main/layout.html')





