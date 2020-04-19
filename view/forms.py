
from django.forms import ModelForm

from .models import People

class PeoplesForm(ModelForm):
    class Meta:
        model = People
        fields = ('Name', 'YearsOne', 'YearsTwo', 'Place')
