from django.urls import path
from .views import HomePageView # home

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    #path('', home, name="home")
]