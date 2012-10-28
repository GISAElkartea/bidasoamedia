from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from infinite_pagination import InfinitePaginator

from project.articles.models import Article, Category


class ArticleList(ListView):
    queryset = Article.objects.published()
    allow_empty = True
    paginate_by = 10
    paginator_class = InfinitePaginator
    template_name = 'articles/article_list.yammy'
    context_object_name = 'article_list'


class ArticleCategory(ArticleList):
    def get_queryset(self, *args, **kwargs):
        q = super(ArticleCategory, self).get_queryset(*args, **kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return q.filter(categories=category)

        
class ArticleDetail(DetailView):
    template_name = 'articles/article_detail.yammy'
    queryset = Article.objects.published()
