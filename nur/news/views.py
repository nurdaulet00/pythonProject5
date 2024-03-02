from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView
def news_home(request):
    news = News.objects.order_by('-date')
    return render(request, 'news/novosti.html', {'news': news})

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/details.html'
    context_object_name = 'new'

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/create.html'
    form_class = NewsForm

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = '/news/'

def create(request):
    error = ''
    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('novosti')
        else:
            error = 'Форма была неверной'

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)
