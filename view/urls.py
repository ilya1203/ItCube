from django.urls import path

from django.contrib.auth.views import LoginView
from .views import index, PeopleCreateView

urlpatterns = [
     path('add/', PeopleCreateView.as_view(), name='add'),
     path('login/', LoginView.as_view(), name='login' ),
     path('<int:page_id>/', index, name='index'),
]

# Create your views here.
