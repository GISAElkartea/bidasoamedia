from django.views.generic import DetailView

from project.flat.models import Flatpage


class FlatpageDetail(DetailView):
    model = Flatpage
    template_name = 'flat/flat_detail.html'
    context_object_name = 'flatpage'
