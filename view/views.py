from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import People
from .forms import PeoplesForm
def index(request, page_id):
    cont = People.objects.order_by('Name')[20*(page_id-1):20*page_id]
    if page_id == 1:
        but = [page_id,page_id+1, page_id+2, page_id+3, page_id+4]
    elif page_id == 2:
        but = [page_id-1,page_id,page_id+1, page_id+2, page_id+3, ]
    elif page_id >= 82:
         but = [80,81,82,83, 84, ]
    elif page_id > 2:
        but = [page_id-2,page_id-1,page_id, page_id+1, page_id+2, ]
    return render(request, 'ItCube/index.html', {'cont': cont, 'pp': page_id, 'but':but})

class PeopleCreateView(CreateView):
    template_name = 'ItCube/index.html'
    form_class = PeoplesForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = {'conf': 'adds'}
        cc2 = {**context, **x} 
        return cc2
