from django.views.generic import View, ListView
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Soundcloud, Pic, About, Instagram
from .forms import ContactForm


class LandingPage(View):
    def get(self, *args, **kwargs):
        return render(self.request, "landing.html", status=200)


class HomePage(View):
    def get(self, *args, **kwargs):
        return render(self.request, "home.html", status=200)


class AboutView(ListView):
    context_object_name = 'info'
    paginate_by = 1
    template_name = 'about.html'
    queryset = Pic.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about'] = About.objects.all()
        context['pics'] = self.queryset
        return context


class MixListView(ListView):
    model = Soundcloud
    paginate_by = 8
    template_name = "mixes-and-tracks.html"


class SocialMediaView(View):
    def get(self, *args, **kwargs):
        igs = Instagram.objects.all()
        context = {
            "igs": igs
        }
        return render(self.request, "social-media.html", context, status=200)


class StreamsView(View):
    def get(self, *args, **kwargs):
        context = {}
        return render(self.request, "streams.html", context, status=200)


class ContactView(View):
    def get(self, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(self.request, "contact.html", context, status=200)

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST or None)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['blvksite.page@gmail.com'])
                messages.success(self.request, "Your message has been sent!")
                return redirect("core:contact")
            except BadHeaderError:
                messages.error(self.request, "Invalid header found. Try again.")
                return redirect("core:contact")
            except Exception as e:
                messages.error(self.request, "Something went wrong. Please try again.")
                return redirect("core:contact")
