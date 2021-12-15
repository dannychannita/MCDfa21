from django.urls import path
from .views import HomePageView, AboutPageView, ReviewsPageView, BlogListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('reviews/', ReviewsPageView.as_view(), name='reviews'),
#    path('', BlogListView.as_view(), name='home'),
]

