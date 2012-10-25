from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from project.articles.models import Article, Category


class ArticleCategory(ListView):
    template_name = 'articles/article_list.yammy'
    allow_empty = True

    def get_queryset(self, *args, **kwargs):
        q = super(ArticleCategory, self).get_queryset(*args, **kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return q.filter(categories=category)

        
class ArticleList(ListView):
    template_name = 'articles/article_list.yammy'
    queryset = Article.objects.published()
    allow_empty = True


class ArticleDetail(DetailView):
    template_name = 'articles/article_detail.yammy'
    queryset = Article.objects.published()
