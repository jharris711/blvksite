from django.urls import path, include
from .views import (
    LandingPage,
    HomePage,
    MixListView,
    SocialMediaView,
    StreamsView,
    ContactView,
    AboutView,
)


app_name = 'core'


urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('home/', HomePage.as_view(), name='home'),
    path('mixes-and-tracks/', MixListView.as_view(), name="mixes"),
    path('social-media/', SocialMediaView.as_view(), name="social"),
    path('streams/', StreamsView.as_view(), name="streams"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('about/', AboutView.as_view(), name="about"),
]
