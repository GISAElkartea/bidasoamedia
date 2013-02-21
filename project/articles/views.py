from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from infinite_pagination import InfinitePaginator

from project.articles.models import Article, Category


class ArticleList(ListView):
    allow_empty = True
    paginate_by = 10
    paginator_class = InfinitePaginator
    template_name = 'articles/article_list.yammy'
    context_object_name = 'article_list'

    def get_queryset(self, *args, **kwargs):
        return Article.objects.published()


class ArticleCategory(ArticleList):
    def get_queryset(self, *args, **kwargs):
        q = super(ArticleCategory, self).get_queryset(*args, **kwargs)
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return q.filter(categories=self.category)

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleCategory, self).get_context_data(*args, **kwargs)
        context['category'] = self.category
        return context

        
class ArticleDetail(DetailView):
    template_name = 'articles/article_detail.yammy'
    queryset = Article.objects.published()

    def get_queryset(self, *args, **kwargs):
        return Article.objects.published()
