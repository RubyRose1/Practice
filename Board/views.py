from django.shortcuts import render, get_object_or_404

from Board.models import Article


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, "Board/home.html", context)


def about(request):
    return render(request, 'Board/about.html')

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request,'Board/article.html',{'article':article})
