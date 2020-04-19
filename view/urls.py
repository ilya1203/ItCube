from django.urls import path

from .views import index, PeopleCreateView

urlpatterns = [
     path('add/', PeopleCreateView.as_view(), name='add'),
     path('<int:page_id>/', index, name='index'),
]

# Create your views here.
