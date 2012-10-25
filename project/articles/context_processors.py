from project.articles.models import Category


def categories(request):
    return {'category_list': Category.objects.all()}
