from django.urls import path
from .views import HomePageView, AboutPageView
from .views import ReviewsPageView  # new

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('', ReviewsPageView.as_view(), name='reviews'),
]
