from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from FastMark.models import Article, Author, Comment

# articles = [
#    {
#        'id': 1,
#        'title': 'First news',
#        'text': 'This is the worst first article'
#    },
#    {
#        'id': 2,
#        'title': 'Second news',
#        'text': 'This is the amazing second article'
#    }
# ]

# Create your views here.
def index(request):
    articles = Article.objects.order_by("created_date")
    return render(request, 'FastMark/news_list.html', 
                {
                    "articles": articles,
                    "count_articles": len(articles)
                })

def get_article(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
        bauthor = Author.objects.filter(article__pk = article_id)
        comments = Comment.objects.filter(article = article_id)
    except Article.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'FastMark/news_article.html', 
                  {
                    'article': article,
                    'author': bauthor,
                    'comments': comments
                    })

def get_about(request):
    return render(request, 'FastMark/about.html')