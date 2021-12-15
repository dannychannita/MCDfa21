from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView): #new
    template_name = 'about.html'


class ReviewsPageView(TemplateView): #new
    template_name = 'ReviewsPage.html'

