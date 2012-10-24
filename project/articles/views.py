from django.views.generic import ListView, DetailView

from project.articles.models import Article, Category


class ArticleList(ListView):
    template_name = 'articles/article_list.yammy'
    model = Article
