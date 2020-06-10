from django.urls import path, include
from .views import LandingPage, HomePage, MixListView


app_name = 'core'


urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('home/', HomePage.as_view(), name='home'),
    path('mixes-and-tracks/', MixListView.as_view(), name="mixes")
]
