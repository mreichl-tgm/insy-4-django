from django.views import generic

from .models import Land


class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'laender'

    def get_queryset(self):
        return Land.objects.all()
