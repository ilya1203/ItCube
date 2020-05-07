from django.urls import path

from django.contrib.auth.views import LoginView
from .views import index, PeopleCreateView, SearchResultsView


urlpatterns = [
     path('add/', PeopleCreateView.as_view(), name='add'),
     path('login/', LoginView.as_view(), name='login' ),
     path('search/', SearchResultsView.as_view(), name='search_results'),
     path('<int:page_id>/', index, name='index'),
]

# Create your views here.
