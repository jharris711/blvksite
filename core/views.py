from django.views.generic import View, ListView
from django.shortcuts import render
from .models import Soundcloud


class LandingPage(View):
    def get(self, *args, **kwargs):
        return render(self.request, "landing.html", status=200)


class HomePage(View):
    def get(self, *args, **kwargs):
        return render(self.request, "home.html", status=200)


class MixListView(ListView):
    model = Soundcloud
    paginate_by = 8
    template_name = "mixes-and-tracks.html"
