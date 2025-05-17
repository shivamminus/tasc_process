from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class LandingPageView(APIView):
    def get(self, request):
        return Response({
            "welcome": "Welcome to the Architectural Governance Portal.",
            "about": "Understand the importance of architectural review and compliance with the company's control procedures for a secure software supply chain.",
            "features": [
                "Team Registration",
                "Criteria Review",
                "Evidence Submission",
                "Save for Later"
            ],
            "cta": "Start your architectural review journey or contact the review team."
        })


from .models import Testimonial
from .serializers import TestimonialSerializer
from rest_framework.generics import ListAPIView

class TestimonialListView(ListAPIView):
    queryset = Testimonial.objects.all().order_by('-created_at')
    serializer_class = TestimonialSerializer