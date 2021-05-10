from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import serializers, viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
                'course', 'message', 'rating'
                )
 

# @api_view(["GET", "POST", "PUT"])
# @csrf_exempt
class FeedbackViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
