from django.urls import path
from .views import LandingPageView, TestimonialListView

urlpatterns = [
    path('landing/', LandingPageView.as_view(), name='landing-page'),
    
    path('testimonials/', TestimonialListView.as_view(), name='testimonials'),
]
