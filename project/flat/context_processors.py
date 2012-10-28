from project.flat.models import Flatpage


def flatpage_list(request):
    return {'flatpage_list': Flatpage.objects.all()}
