from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})



def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')  # Rediriger vers la liste des articles après l'ajout
    else:
        form = ArticleForm()
    return render(request, 'articles/add_article.html', {'form': form})
